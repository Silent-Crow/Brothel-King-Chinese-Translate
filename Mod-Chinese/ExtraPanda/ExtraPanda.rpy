# 内容扩展 V1.0
## 91Panda 制作 2025-2-15
## 适用于青楼之王0.3版本



init 900 python:


    config.label_overrides["init_postings"] = "Panda_init_postings"

    ExtraPanda_template = Mod(
        
                ## 模组基础信息 (注意: 版本号将用于检查模组是否是最新版本。 Failure to update the version number may lead to broken mods and saved games)
                name = "内容扩展",
                folder = "ExtraPanda",
                creator = "PANDA",
                version = 1.1,
                pic = "封面.jpg",
                description = """现在这里有更多种类的委托和培训课程可供选择。\n本模组仅扩展了文本内容，并无属性改动。""",

                ## 事件字典 (所有的模组事件都应该在这里设置)
                )

    def extra_panda_randomize(self, rank):

        self.enrolled = []
        self.rank = round_int(rank)

        ## Randomize picture

        self.pic = get_pic(quest_board, self.tags)

        ## Set duration
        self.duration = max(dice(2 + rank//2), rank//2) # Rank 1: 1-2d Rank 2: 1-3d Rank 3: 2-3d Rank 4: 2-4d Rank 5: 2-4d

        ## Test special status

        if dice(6) == 6:
            if self.type == "class":
                self.special = rand_choice((_("Cheap"), _("Masterclass")))
            elif self.type == "quest":
                self.special = rand_choice((_("High reward"), _("Notorious")))
        else:
            self.special = None

        ## Set bonus and stat cap for classes

        if self.type == "class":

            self.bonuses = []

            #? Improved bonuses with rank
            self.bonuses.append([self.main_stat, self.duration*2 + rank, self.duration*4 + rank]) # Stores min/max bonuses to stat per day

            if rank > 1 and dice(100) < (rank-1) * 25: # Chance of adding second bonus at higher ranks
                self.bonuses.append([self.secondary_stat, self.duration + rank//1.5, self.duration*3 + rank//1.5]) # Stores min/max bonuses to stat per day
            if rank > 3 and dice(100) < (rank-3) * 25: # Chance of adding third bonus at higher ranks
                self.bonuses.append([rand_choice(self.other_stats), self.duration-1 + rank//2, self.duration*2 + rank//2]) # Stores min/max bonuses to stat per day

            self.stat_cap = 55 * rank #? Experimental

            self.capacity = 1 + dice(rank+1)


        ## Randomize stat requirements for quests

        if self.type == "quest":

            self.requirements = []

            # Normal stats have higher requirements than sx stats at earlier ranks then converge at rank 5
            if self.main_stat.capitalize() in gstats_main:
                self.requirements.append([self.main_stat, 20 * rank + dice(40, rank)])

            else:
                self.requirements.append([self.main_stat, 4 * rank**2 + dice(40, rank)])

            if dice(100) < (rank - 1) * 25: # Chance of adding second requirement at higher ranks

                if self.main_stat.capitalize() in gstats_main:
                    self.requirements.append([self.secondary_stat, 20 * (rank-1) + dice(40, rank-1)])

                else:
                    self.requirements.append([self.secondary_stat, 4 * (rank-1)**2 + dice(40, rank-1)])

            if dice(100) < (rank - 2) * 25: # Chance of adding third requirement at higher ranks

                if self.main_stat.capitalize() in gstats_main:
                    self.requirements.append([rand_choice(self.other_stats), 20 * (rank-1) + dice(40, rank-1)])

                else:
                    self.requirements.append([rand_choice(self.other_stats), 4 * (rank-1)**2 + dice(40, rank-1)])


        ## Add 2 positive + 1 negative traits

        self.pos_traits = rand_choice(gold_traits + pos_traits, 2)

        self.neg_trait = rand_choice(neg_traits)


        ## Calculate rewards and costs

        if self.type == "quest":

            self.gold = 25*rank**2
            self.xp = 0
            self.rep = 0

            # Values have yet to be play-tested to make sure nothing is broken

            for stat, value in self.requirements:

                if stat in gstats_main:
                    self.gold += value * quest_base_gold["normal"]
                    self.rep += 2 ** (rank-1)

                else:
                    self.gold += value * quest_base_gold["sex"]
                    self.rep += 2 * (2 ** (rank-1))

                self.xp += value * rank

            # Apply duration bonus (long quests bring more cash, short quests are good for rep)

            self.gold *= self.duration + 0.05*(self.duration-1)
            self.rep *= 1 + 0.05*(self.duration-1)
            self.xp *= self.duration

            if self.special == "High reward":
                self.gold *= 2

            self.gold = round_int(self.gold * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))
            self.rep = round_int(self.rep * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))
            self.xp = round_int(self.xp * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))

        elif self.type == "class":

            self.gold = 25*rank**2

            for stat, _min, _max in self.bonuses:
                if stat in gstats_main:
                    self.gold += (_min+_max)/2 * 5
                else:
                    self.gold += (_min+_max)/2 * 10

            self.xp = (10 * rank**2) * self.duration * game.get_diff_setting("rewards") #? Experimental
            self.rep = (1 + 0.05*(self.duration-1)) * 2**(rank-1) * game.get_diff_setting("rewards")

            if self.special == "Cheap":
                self.gold = round_int(0.5*self.gold)

        self.energy = -5 * rank * self.duration
    Quest.randomize = extra_panda_randomize

    # 添加新的任务和课程  

label Panda_init_postings():
    python:
        # 任务委托 #

        quest_templates = [
                            Quest("quest", name = '平面模特', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我需要一位美丽的女士来做我的平面模特，帮助我设计出新款式的衣服。","我新设计了一款暴露的内衣，需要模特试穿看看效果。"]), sound = s_sigh),
                            Quest("quest", name = '招募舞伴', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["我需要一位舞姿优美的舞伴，能让我在舞会上不输给其他人。","我新买了几套异域风情的舞裙，想找一位性感的舞娘和我一起共舞。"]), sound = s_sigh),
                            Quest("quest", name = '宴会准备', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["老爷的生辰就快到了，我们宴请了亲朋好友，现在需要更多的人手帮忙布置晚宴现场。","宴会的餐碟不够了，管家提议举办一场女体盛，需要丰满的女性充当容器。"]), sound = s_sigh),
                            Quest("quest", name = '临时女伴', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["老同学约我聚会，我需要带上一位高贵优雅的女伴让他们惊掉下巴。","我要出席一场晚会，没有女伴怎么能行，我准备好了性感的晚礼服，急需一位美女与我作伴。"]), sound = s_sigh),
                            
                            Quest("quest", name = '枯木逢春', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我已经好久没有体验过真正的性爱了，希望有人能帮我枯木逢春。","我感觉寻常的性爱已经提不起兴趣了，谁能帮我唤醒沉睡的巨龙？"]), sound = s_aaha),
                            Quest("quest", name = '突破记录', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我打算挑战世界做爱纪录，为此我需要有人陪我练习!","为了打破季伯长创造的做爱记录，我需要有人协助我一起练习。"]), sound = s_aaha),
                            Quest("quest", name = '租赁女友', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["家里总是在催我相亲，我需要找一位临时的女友应付一下。当然做戏要做到位。","我和朋友吹牛说自己有一个漂亮的女朋友，他们非要亲眼见一见，我在酒店开好了房间，急需一位女友。"]), sound = s_aaha),
                            Quest("quest", name = '家政清洁', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["我需要家政清理我的房间，要求必须穿上特殊的女仆装。","我的泳池很久没用过了，现在里面全是绿藻，我需要一位家政人士穿着性感的比基尼去清理一下泳池。"]), sound = s_aaha),
                            
                            Quest("quest", name = '家庭教师', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我的儿子已经二十岁了，还没破处，我需要一位生理老师指导他一二。","我们需要一位富有实战经验的生理老师，教这些涉世未深的贵族小姐们传授如何侍奉未来的丈夫。"]), sound = s_mmmh),
                            Quest("quest", name = '寻欢作乐', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["我想找点乐子，玩点新花样，最好是不带套的那种。","我好寂寞啊，期待一场美妙的邂逅或者一夜情。"]), sound = s_mmmh),
                            Quest("quest", name = '赏菊大会', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["仅限年轻女性，记得清洗干净，嫩菊才最有韵味。","身材娇小的可爱女性更受我们的欢迎。"]), sound = s_mmmh),
                            Quest("quest", name = '地牢之夜', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["招募女性参加我们的活动，放心不会有任何伤害，我们也会为你购买保险的。","在地牢中和触手怪大战三百回合，最终获胜的战士将会获得巨额的奖励————一大桶精液。"]), sound = s_mmmh),
                            
                            Quest("quest", name = '轰趴派对', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'group', description = random.choice(["我打算在家里的别墅举办一场淫乱的派对，性感的女孩越多越好。","明天我要在家举办一场狂欢派对，记得穿的单薄一点这样香槟才能浸湿你的衣服。"]), sound = s_aah),
                            Quest("quest", name = '假面舞会', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'group', description = random.choice(["我们打算举办一场联谊会，为了增进大家的感情特地安排了一场假面舞会，需要一些女性来撑撑场面。","在假面之下没人知道你的真实身份，尽情地狂欢吧！抛下那些无用的衣服和世俗道德，这里是肉欲的天堂。"]), sound = s_aah),

                #扩展任务#            
                            Quest("quest", name = '人体模特', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我的素描课需要一位人体模特，学生们都等不及了。","我需要一位裸体模特来为学徒讲解人体构造。"]), sound = s_sigh),
                            Quest("quest", name = '舞蹈老师', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["为了在晚会上表演节目，我需要一位舞蹈老师指导她们的动作。","有没有老师愿意贴身指导我舞姿，不要太在意肢体接触，那是难以避免的嘛。"]), sound = s_sigh),
                            Quest("quest", name = '打扫卫生', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["宴会之后留下了一地的狼藉，我们需要更多的人手快速清理现场。","酒店的房间昨天被那些小情侣弄得一团乱，我需要更多的人手帮忙清理房间。"]), sound = s_sigh),
                            Quest("quest", name = '开业表演', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["我的新店即将开张，需要有人在门前表演揽客。","我需要一些性感的美女帮我招揽顾客。"]), sound = s_sigh),
                            
                            Quest("quest", name = '走出阴影', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我刚刚和女朋友分手了，我需要有人帮我走出失恋的阴影。","我的母亲去世不久，我需要一个成熟性感的女性弥补我缺失的母爱。"]), sound = s_aaha),
                            Quest("quest", name = '明星应援', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我们需要更多的粉丝为偶像应援，在台下欢呼喝彩，挥舞应援棒。","演唱会即将举办，我需要一些人扮演狂热的粉丝给歌手献花，最好是献身..."]), sound = s_aaha),
                            Quest("quest", name = '时装展览', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["本公司的新品发布会需要模特穿着新款时装在T台走秀，免费穿新款的机会可不多，快来吧！","时装周要到了，我需要一些模特穿着样品在展台上“搔首弄姿”。"]), sound = s_aaha),
                            Quest("quest", name = '修剪草坪', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'fetish', description = random.choice(["花园的杂草又长得到处都是，我需要有人清理掉这些废物。","我的高尔夫球场上长出了许多杂草，快帮我清理掉这些该死的刺头。"]), sound = s_aaha),
                            
                            Quest("quest", name = '家庭护理', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我受了很重的伤没办法自理，我需要有人照顾我，以及处理性欲。","我的父亲卧床不起，我有事要出门，需要一位护工临时照顾他的起居，他最爱喝奶。"]), sound = s_mmmh),
                            Quest("quest", name = '动作指导', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["我们的演员没有经验，拍不好床戏，需要有人一对一贴身指导一下他。","我的色情漫画画到关键剧情卡住了，我需要有人摆出特定的姿势供我参考。"]), sound = s_mmmh),
                            Quest("quest", name = '研发新药', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["本公司研发了一种新型药剂，需要实验者，需要从后面注射进去，然后塞上肛塞确保药剂不会流出来。","本公司研发了一种新型灌肠药水，可以快速清洁肠道，需要实验者。"]), sound = s_mmmh),
                            Quest("quest", name = '宠物伴侣', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["我心爱的宠物离我而去了，我需要一只可爱的新宠物，我准备了纯金镶钻的项圈。","我想养一只贵妇犬，现在犬有了，缺少一位“贵妇”。"]), sound = s_mmmh),

                        ]

        # 培训课程 #

        #原版课程#
        class_templates = [
                        Quest("class", name = '模特培训', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["注意你的体态，步伐。挺胸，收腹，提臀！一，二，三走。","由当红模特亲自授课指导，快速提升你的体态。"]), sound = s_sigh),
                        Quest("class", name = '舞蹈培训', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["拉丁，芭蕾，爵士，交际舞，只要你想，我们什么都教。","由舞林大会亚军舞者亲自授课指导，快速提升你的舞姿，舞姿可不能不行。"]), sound = s_sigh),
                        Quest("class", name = '礼仪培训', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["注意你的仪态，不要像个乡野村妇一样粗鲁，要记得笑不露齿。","花费重金从宫中请来的嬷嬷会亲自指导你的仪态，把你变得像公主一样尊贵。"]), sound = s_sigh),
                        Quest("class", name = '表演培训', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["模拟现场被观众围观的环境，克服你的怯场，自信起来！","知名导演亲自指导，帮你迅速进入状态，摆脱内向。"]), sound = s_sigh),
                        Quest("class", name = '按摩培训', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["掌握合适的力道，使用正确的手法才能让按摩效果事半功倍。","在双乳上涂抹精油，用你的蓓蕾刺激客人的皮肤，在肌肤的亲密接触中让客人体验升天般的快感吧。"]), sound = s_aaha),
                        Quest("class", name = '游泳培训', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["打水，换气，展臂。挑选合适的泳衣，成为水中最快的美人鱼吧。","办卡更优惠哦，在恒温泳池里尽情地畅游吧。"]), sound = s_aaha),
                        Quest("class", name = '美声培训', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["先从发声练习开始，然后掌握换气技巧，学会使用假声。","由二线歌手亲自指导，教你轻松掌握不同的音域和声线。"]), sound = s_aaha),
                        Quest("class", name = '女仆培训', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["一个合格的女仆应该让主人完全不用为琐事操心。","身为女仆应该什么都要会一些，包括处理主人的性欲。"]), sound = s_aaha),
                        Quest("class", name = '侍奉讲座', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["学会侍奉你的主人，注意你的表情和语气，动作和姿势。","假装自己很满足，这会让男性充满自信。"]), sound = s_aah),
                        Quest("class", name = '性爱讲座', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["女孩子要学会保护自己，错误的姿势会让你在做爱时受到伤害。","学会计算自己的安全期，这样才不用为避孕而烦恼。"]), sound = s_aah),
                        Quest("class", name = '肛交讲座', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["由肛交大师亲自授课，为你讲解肛交时的注意事项，最重要的是做好清洁。","做好热身，多多提肛，这样才能让你的肠壁紧缩牢牢地裹住肉棒。"]), sound = s_scream),
                        Quest("class", name = '调教讲座', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["调教可不是单方面的凌虐，这需要双方都积极配合参与。","磨练意志，提高心性，这会让你顺利度过一切苦难。"]), sound = s_scream),
                            
        #扩展课程#                    
                        Quest("class", name = '养颜讲座', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["饮食要清淡，要减少碳水摄入。每天要规律作息，这样才能拥有水润弹性有光泽的皮肤。","人到中年不得已，保温杯里泡枸杞。"]), sound = s_sigh),
                        Quest("class", name = '健美课程', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["先来一组深蹲，再做一组俯卧撑，怕吃苦怎么行！","一对一的私教课程，自己练很容易动作变形，那可太糟糕了。"]), sound = s_sigh),
                        Quest("class", name = '化妆教学', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["合理的妆容搭配不同的服饰才能起到锦上添花的作用，哪有人淡妆浓抹总相宜的。","并不是越昂贵的化妆品效果就越好，要学会搭配。"]), sound = s_sigh),
                        Quest("class", name = '体态纠正', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["腰板挺直别驼背，脚与肩同宽，手摆在腰旁，目视前方！","高抬腿，一字马，拉伸你的韧带，锻炼你的关节。"]), sound = s_sigh),
                        Quest("class", name = '穴位讲解', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["学习人体的各种穴位，刺激它们会起到不同的效果，比如增强性欲和持久力。","清楚地掌握自己的G点在哪里，这样才能更好的配合你的伴侣。"]), sound = s_aaha),
                        Quest("class", name = '瑜伽课程', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["先进入冥想状态，想象自己是一团水，然后放松，自由地挪动你的肢体。","提高身体的柔韧度和伸展能力，这样才能在床上轻松地摆出各种姿势，给他一个惊喜吧！"]), sound = s_aaha),
                        Quest("class", name = '茶艺教室', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["可别毁了一壶好茶，从挑选茶叶开始到沏茶都很有讲究，这里面的门道可深着呢。","提升茶叶口感的一个秘方是鲜榨的母乳，让我们来教你如何催乳。"]), sound = s_aaha),
                        Quest("class", name = '餐桌礼仪', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["在主人动筷子之前要保持静坐，刀叉位置腰摆放正确，碰杯时杯口要微微朝下。","将你的肉体锻炼成餐盘和酒皿，让大家大快朵颐。"]), sound = s_aaha),
                        Quest("class", name = '角色扮演', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["护士，教师，警察，猫娘。打扮成男人最喜欢的模样吧！","男人总会幻想遥亵高高在上的大人物，我们能让他们圆梦。"]), sound = s_aah),
                        Quest("class", name = '子宫按摩', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["平躺屈腿，用大鱼际肌挤压子宫底，轻轻地向上推，慢慢的揉。","适当的锻炼能大幅提高子宫和小穴的敏感度，并增加受孕概率。"]), sound = s_aah),
                        Quest("class", name = '后庭开发', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["使用最新的器械，帮助你扩张你的后庭，这是完全无痛的，甚至还有点舒服。","想象一下一根可以控制的尾巴塞在你的屁股里，左右摇摆，多可爱啊。"]), sound = s_scream),
                        Quest("class", name = '道具练习', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["鞭子，蜡烛，手铐，捆绑...帮助你熟练地掌握各种道具的使用方法。","随课赠送练习用的道具和说明书，质量可靠还免运费。"]), sound = s_scream),                            
                            
                        ]

    return

