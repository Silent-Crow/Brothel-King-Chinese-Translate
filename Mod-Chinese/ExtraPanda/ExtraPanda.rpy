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
                version = 1.0,
                pic = "封面.jpg",
                description = """现在这里有更多种类的委托和培训课程可供选择。\n本模组仅扩展了文本内容，并无属性改动。""",

                ## 事件字典 (所有的模组事件都应该在这里设置)
                )

    # 添加新的任务和课程  

label Panda_init_postings():
    python:
        # 任务委托 #

        quest_templates = [
                            Quest("quest", name = '平面模特', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我需要一位美丽的女士来做我的平面模特，帮助我设计出新款式的衣服。"]), sound = s_sigh),
                            Quest("quest", name = '招募舞伴', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["我需要一位舞姿优美的舞伴，能让我在舞会上不输给其他人。"]), sound = s_sigh),
                            Quest("quest", name = '宴会准备', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["老爷的生辰就快到了，我们宴请了亲朋好友，现在需要更多的人手帮忙布置晚宴现场。"]), sound = s_sigh),
                            Quest("quest", name = '临时女伴', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["老同学约我聚会，我需要带上一位高贵优雅的女伴让他们惊掉下巴。"]), sound = s_sigh),
                            
                            Quest("quest", name = '枯木逢春', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我已经好久没有体验过真正的性爱了，希望有人能帮我枯木逢春。"]), sound = s_aaha),
                            Quest("quest", name = '突破记录', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我打算挑战世界做爱纪录，为此我需要有人陪我练习!"]), sound = s_aaha),
                            Quest("quest", name = '租赁女友', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["家里总是在催我相亲，我需要找一位临时的女友应付一下。当然做戏要做到位。"]), sound = s_aaha),
                            Quest("quest", name = '家政清洁', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["我需要家政清理我的房间，要求必须穿上特殊的女仆装。"]), sound = s_aaha),
                            
                            Quest("quest", name = '家庭教师', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我的儿子已经二十岁了，还没破处，我需要一位生理老师指导他一二。"]), sound = s_mmmh),
                            Quest("quest", name = '寻欢作乐', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["我想找点乐子，玩点新花样，最好是不带套的那种。"]), sound = s_mmmh),
                            Quest("quest", name = '赏菊大会', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["仅限年轻女性，记得清洗干净，嫩菊才最有韵味。"]), sound = s_mmmh),
                            Quest("quest", name = '地牢之夜', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["招募女性参加我们的活动，放心不会有任何伤害，我们也会为你购买保险的。"]), sound = s_mmmh),
                            
                            Quest("quest", name = '轰趴派对', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'group', description = "我打算在家里的别墅举办一场淫乱的派对，性感的女孩越多越好。", sound = s_aah),
                            Quest("quest", name = '假面舞会', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'group', description = "我们打算举办一场联谊会，为了增进大家的感情特地安排了一场假面舞会，需要一些女性来撑撑场面。", sound = s_aah),

                #扩展任务#            
                            Quest("quest", name = '人体模特', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我的素描课需要一位人体模特，学生们都等不及了。"]), sound = s_sigh),
                            Quest("quest", name = '舞蹈老师', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["为了在晚会上表演节目，我需要一位舞蹈老师指导她们的动作。"]), sound = s_sigh),
                            Quest("quest", name = '打扫卫生', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["宴会之后留下了一地的狼藉，我们需要更多的人手快速清理现场。"]), sound = s_sigh),
                            Quest("quest", name = '开业表演', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["我的新店即将开张，需要有人在门前表演揽客。"]), sound = s_sigh),
                            
                            Quest("quest", name = '走出阴影', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我刚刚和女朋友分手了，我需要有人帮我走出失恋的阴影。"]), sound = s_aaha),
                            Quest("quest", name = '明星应援', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我们需要更多的粉丝为偶像应援，在台下欢呼喝彩，挥舞应援棒。"]), sound = s_aaha),
                            Quest("quest", name = '时装展览', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["本公司的新品发布会需要模特穿着新款时装在T台走秀，免费穿新款的机会可不多，快来吧！"]), sound = s_aaha),
                            Quest("quest", name = '修剪草坪', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'fetish', description = random.choice(["花园的杂草又长得到处都是，我需要有人清理掉这些废物。"]), sound = s_aaha),
                            
                            Quest("quest", name = '家庭护理', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我受了很重的伤没办法自理，我需要有人照顾我，以及处理性欲。"]), sound = s_mmmh),
                            Quest("quest", name = '动作指导', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["年轻的演员没有经历过激烈的性爱，拍不好床戏，我们需要专家来提供动作指导。"]), sound = s_mmmh),
                            Quest("quest", name = '研发新药', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["本公司研发了一款新型栓剂，需要试药者从肛门插入吸收，观察药物效果。"]), sound = s_mmmh),
                            Quest("quest", name = '发泄压力', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["我积攒了许多压力，我需要有人帮我发泄发泄。"]), sound = s_mmmh),

                        ]

        # 培训课程 #

        #原版课程#
        class_templates = [
                        Quest("class", name = '模特培训', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["注意你的体态，步伐。挺胸，收腹，提臀！一，二，三走。"]), sound = s_sigh),
                        Quest("class", name = '舞蹈培训', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["拉丁，芭蕾，爵士，交际舞，只要你想，我们什么都教。"]), sound = s_sigh),
                        Quest("class", name = '礼仪培训', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["注意你的仪态，不要像个乡野村妇一样粗鲁，要记得笑不露齿。"]), sound = s_sigh),
                        Quest("class", name = '表演培训', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["模拟现场被观众围观的环境，克服你的怯场，自信起来！"]), sound = s_sigh),
                        Quest("class", name = '按摩培训', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["掌握合适的力道，使用正确的手法才能让按摩效果事半功倍。"]), sound = s_aaha),
                        Quest("class", name = '游泳培训', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["打水，换气，展臂。挑选合适的泳衣，成为水中最快的美人鱼吧。"]), sound = s_aaha),
                        Quest("class", name = '美声培训', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["先从发声练习开始，然后掌握换气技巧，学会使用假声。"]), sound = s_aaha),
                        Quest("class", name = '女仆培训', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["一个合格的女仆应该让主人完全不用为琐事操心。"]), sound = s_aaha),
                        Quest("class", name = '侍奉讲座', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["学会侍奉你的主人，注意你的表情和语气，动作和姿势。"]), sound = s_aah),
                        Quest("class", name = '性爱讲座', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["女孩子要学会保护自己，错误的姿势会让你在做爱时受到伤害。"]), sound = s_aah),
                        Quest("class", name = '肛交讲座', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["由肛交大师亲自授课，为你讲解肛交时的注意事项，最重要的是做好清洁。"]), sound = s_scream),
                        Quest("class", name = '调教讲座', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["调教可不是单方面的凌虐，这需要双方都积极配合参与。"]), sound = s_scream),
                            
        #扩展课程#                    
                        Quest("class", name = '养颜讲座', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["饮食要清淡，要减少碳水摄入。每天要规律作息，这样才能拥有水润弹性有光泽的皮肤。"]), sound = s_sigh),
                        Quest("class", name = '健美课程', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["先来一组深蹲，再做一组俯卧撑，怕吃苦怎么行！"]), sound = s_sigh),
                        Quest("class", name = '化妆教学', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["合理的妆容搭配不同的服饰才能起到锦上添花的作用，哪有人淡妆浓抹总相宜的。"]), sound = s_sigh),
                        Quest("class", name = '体态纠正', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["腰板挺直别驼背，脚与肩同宽，手摆在腰旁，目视前方！"]), sound = s_sigh),
                        Quest("class", name = '穴位讲解', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["学习人体的各种穴位，刺激它们会起到不同的效果，比如增强性欲和持久力。"]), sound = s_aaha),
                        Quest("class", name = '瑜伽课程', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["先进入冥想状态，想象自己是一团水，然后放松，自由地挪动你的肢体。"]), sound = s_aaha),
                        Quest("class", name = '茶艺教室', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["可别毁了一壶好茶，从挑选茶叶开始到沏茶都很有讲究，这里面的门道可深着呢。"]), sound = s_aaha),
                        Quest("class", name = '餐桌礼仪', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["在主人动筷子之前要保持静坐，刀叉位置腰摆放正确，碰杯时杯口要微微朝下。"]), sound = s_aaha),
                        Quest("class", name = '角色扮演', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["护士，教师，警察，猫娘。打扮成男人最喜欢的模样吧！"]), sound = s_aah),
                        Quest("class", name = '子宫按摩', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["平躺屈腿，用大鱼际肌挤压子宫底，轻轻地向上推，慢慢的揉。"]), sound = s_aah),
                        Quest("class", name = '后庭开发', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["使用最新的器械，帮助你扩张你的后庭，这是完全无痛的，甚至还有点舒服。"]), sound = s_scream),
                        Quest("class", name = '道具练习', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["鞭子，蜡烛，手铐，捆绑...帮助你熟练地掌握各种道具的使用方法。"]), sound = s_scream),                            
                            
                        ]

    return

