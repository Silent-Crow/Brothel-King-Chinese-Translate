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
                pic = "封面.png",
                description = """公会提高了工作效率，扩建了大厅，现在这里有更多种类的委托和培训课程可供选择。\n本模组仅扩展了文本内容，并无属性改动。""",

                ## 事件字典 (所有的模组事件都应该在这里设置)
                )

    # 添加新的任务和课程  

label Panda_init_postings():

    python:

        # 任务委托 #

        quest_templates = [
            
            #原版任务#
                        Quest("quest", name = '平面模特' main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我需要一位美丽的女士来做我的平面模特，帮助我设计出新款式的衣服。"]), sound = s_sigh),
                        Quest("quest", name = '招募舞伴' main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["我需要一位舞姿优美的舞伴，能让我在舞会上不输给其他人。"]), sound = s_sigh),
                        Quest("quest", name = '宴会准备' main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["老爷的生辰就快到了，我们宴请了亲朋好友，现在需要更多的人手帮忙布置晚宴现场。"]), sound = s_sigh),
                        Quest("quest", name = '临时女伴' main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["老同学约我聚会，我需要带上一位高贵优雅的女伴让他们惊掉下巴。"]), sound = s_sigh),
                        
                        Quest("quest", name = '枯木逢春' main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我已经好久没有体验过真正的性爱了，希望有人能帮我枯木逢春。"]), sound = s_aaha),
                        Quest("quest", name = '突破记录' main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我打算挑战世界做爱纪录，为此我需要有人陪我练习!"]), sound = s_aaha),
                        Quest("quest", name = '租赁女友' main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["家里总是在催我相亲，我需要找一位临时的女友应付一下。当然做戏要做到位。"]), sound = s_aaha),
                        Quest("quest", name = '家政清洁' main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["我需要家政清理我的房间，要求必须穿上特殊的女仆装。"]), sound = s_aaha),
                        
                        Quest("quest", name = '家庭教师' main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我的儿子已经二十岁了，还没破处，我需要一位生理老师指导他一二。"]), sound = s_mmmh),
                        Quest("quest", name = '寻欢作乐' main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["我想找点乐子，玩点新花样，最好是不带套的那种。"]), sound = s_mmmh),
                        Quest("quest", name = '赏菊大会' main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["仅限年轻女性，记得清洗干净，嫩菊才最有韵味。"]), sound = s_mmmh),
                        Quest("quest", name = '地牢之夜' main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["招募女性参加我们的活动，放心不会有任何伤害，我们也会为你购买保险的。"]), sound = s_mmmh),
                        
                        Quest("quest", name = '轰趴派对', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'group', description = "我打算在家里的别墅举办一场淫乱的派对，性感的女孩越多越好。", sound = s_aah),
                        Quest("quest", name = '假面舞会', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'group', description = "我们打算举办一场联谊会，为了增进大家的感情特地安排了一场假面舞会，需要一些女性来撑撑场面。", sound = s_aah),

            #扩展任务#            
                        Quest("quest", name = '人体模特' main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["我的素描课需要一位人体模特，学生们都等不及了。"]), sound = s_sigh),
                        Quest("quest", name = '舞蹈老师' main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["为了在晚会上表演节目，我需要一位舞蹈老师指导她们的动作。"]), sound = s_sigh),
                        Quest("quest", name = '打扫卫生' main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["宴会之后留下了一地的狼藉，我们需要更多的人手快速清理现场。"]), sound = s_sigh),
                        Quest("quest", name = '开业表演' main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["我的新店即将开张，需要有人在门前表演揽客。"]), sound = s_sigh),
                        
                        Quest("quest", name = '走出阴影' main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = random.choice(["我刚刚和女朋友分手了，我需要有人帮我走出失恋的阴影。"]), sound = s_aaha),
                        Quest("quest", name = '明星应援' main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = random.choice(["我们需要更多的粉丝为偶像应援，在台下欢呼喝彩，挥舞应援棒。"]), sound = s_aaha),
                        Quest("quest", name = '时装展览' main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = random.choice(["本公司的新品发布会需要模特穿着新款时装在T台走秀，免费穿新款的机会可不多，快来吧！"]), sound = s_aaha),
                        Quest("quest", name = '修剪草坪' main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'fetish', description = random.choice(["花园的杂草又长得到处都是，我需要有人清理掉这些废物。"]), sound = s_aaha),
                        
                        Quest("quest", name = '家庭护理' main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = random.choice(["我受了很重的伤没办法自理，我需要有人照顾我，以及处理性欲。"]), sound = s_mmmh),
                        Quest("quest", name = '动作指导' main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = random.choice(["年轻的演员没有经历过激烈的性爱，拍不好床戏，我们需要专家来提供动作指导。"]), sound = s_mmmh),
                        Quest("quest", name = '研发新药' main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = random.choice(["本公司研发了一款新型栓剂，需要试药者从肛门插入吸收，观察药物效果。"]), sound = s_mmmh),
                        Quest("quest", name = '发泄压力' main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = random.choice(["我积攒了许多压力，我需要有人帮我发泄发泄。"]), sound = s_mmmh),


                        ]

        # 培训课程 #

        #原版课程#
        class_templates = [
                            Quest("class", name = '模特培训班' main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["Learn the secrets to looking fabulous and have perfect hair at all times! Who wants to look natural anyway?"]), sound = s_sigh),
                            Quest("class", name = '舞蹈培训班' main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["Zomba! Bodyfighting! Aqua reggeaton!\nHurry before we make up even more silly names!"]), sound = s_sigh),
                            Quest("class", name = '女仆培训班' main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["Learn the basics of working tables... You'll never spill a glass on a customer's crotch again, unless you want to!"]), sound = s_sigh),
                            Quest("class", name = '表演培训班' main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["Master all Zanic traditional arts, including the exact science of tea ceremony trigonometry. Don't look like an ass because your tea cup is off 5 degrees to the left!"]), sound = s_sigh),
                            Quest("class", name = '按摩培训班' main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["Spend a relaxing few days at the spa with us. It will be awesome! As for the teaching... Wait, what teaching?"]), sound = s_aaha),
                            Quest("class", name = '游泳培训班' main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["The sun shining on exposed bodies... Water running along voluptuous curves... Tanning oil on glistening skin... And swimming, of course. Erm."]), sound = s_aaha),
                            Quest("class", name = '美声培训班' main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["'Sing properly dammit, or I'll rip off your head and shove manure down your neck!'. How bad can a singing class be? Oh, you'll see..."]), sound = s_aaha),
                            Quest("class", name = '进阶' main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["'If you want to clean up properly, you have to bend forward a lot more! More... More... Hmm, that's better.'"]), sound = s_aaha),
                            Quest("class", name = 'XXX{#1}' main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?{#1}"]), sound = s_aah),
                            Quest("class", name = 'XXX' main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?"]), sound = s_aah),
                            Quest("class", name = 'Hardcore{#1}' main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!{#1}"]), sound = s_scream),
                            Quest("class", name = 'Hardcore{#2}' main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!"]), sound = s_scream),
                            
        #扩展课程#                    
                            Quest("class", name = 'Modeling' main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["Learn the secrets to looking fabulous and have perfect hair at all times! Who wants to look natural anyway?"]), sound = s_sigh),
                            Quest("class", name = 'Dancing' main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["Zomba! Bodyfighting! Aqua reggeaton!\nHurry before we make up even more silly names!"]), sound = s_sigh),
                            Quest("class", name = 'Waitress{#1}' main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["Learn the basics of working tables... You'll never spill a glass on a customer's crotch again, unless you want to!"]), sound = s_sigh),
                            Quest("class", name = 'Geisha{#1}' main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["Master all Zanic traditional arts, including the exact science of tea ceremony trigonometry. Don't look like an ass because your tea cup is off 5 degrees to the left!"]), sound = s_sigh),
                            Quest("class", name = 'Massage' main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["Spend a relaxing few days at the spa with us. It will be awesome! As for the teaching... Wait, what teaching?"]), sound = s_aaha),
                            Quest("class", name = 'Swimming' main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["The sun shining on exposed bodies... Water running along voluptuous curves... Tanning oil on glistening skin... And swimming, of course. Erm."]), sound = s_aaha),
                            Quest("class", name = 'Singing' main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["'Sing properly dammit, or I'll rip off your head and shove manure down your neck!'. How bad can a singing class be? Oh, you'll see..."]), sound = s_aaha),
                            Quest("class", name = 'Maid' main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["'If you want to clean up properly, you have to bend forward a lot more! More... More... Hmm, that's better.'"]), sound = s_aaha),
                            Quest("class", name = 'XXX{#1}' main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?{#1}"]), sound = s_aah),
                            Quest("class", name = 'XXX' main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?"]), sound = s_aah),
                            Quest("class", name = 'Hardcore{#1}' main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!{#1}"]), sound = s_scream),
                            Quest("class", name = 'Hardcore{#2}' main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!"]), sound = s_scream),                            
                            
                            
                            Quest("class", name = 'Modeling' main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = random.choice(["Learn the secrets to looking fabulous and have perfect hair at all times! Who wants to look natural anyway?"]), sound = s_sigh),
                            Quest("class", name = 'Dancing' main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = random.choice(["Zomba! Bodyfighting! Aqua reggeaton!\nHurry before we make up even more silly names!"]), sound = s_sigh),
                            Quest("class", name = 'Waitress{#1}' main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = random.choice(["Learn the basics of working tables... You'll never spill a glass on a customer's crotch again, unless you want to!"]), sound = s_sigh),
                            Quest("class", name = 'Geisha{#1}' main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = random.choice(["Master all Zanic traditional arts, including the exact science of tea ceremony trigonometry. Don't look like an ass because your tea cup is off 5 degrees to the left!"]), sound = s_sigh),
                            Quest("class", name = 'Massage' main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = random.choice(["Spend a relaxing few days at the spa with us. It will be awesome! As for the teaching... Wait, what teaching?"]), sound = s_aaha),
                            Quest("class", name = 'Swimming' main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = random.choice(["The sun shining on exposed bodies... Water running along voluptuous curves... Tanning oil on glistening skin... And swimming, of course. Erm."]), sound = s_aaha),
                            Quest("class", name = 'Singing' main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = random.choice(["'Sing properly dammit, or I'll rip off your head and shove manure down your neck!'. How bad can a singing class be? Oh, you'll see..."]), sound = s_aaha),
                            Quest("class", name = 'Maid' main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = random.choice(["'If you want to clean up properly, you have to bend forward a lot more! More... More... Hmm, that's better.'"]), sound = s_aaha),
                            Quest("class", name = 'XXX{#1}' main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?{#1}"]), sound = s_aah),
                            Quest("class", name = 'XXX' main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = random.choice(["Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?"]), sound = s_aah),
                            Quest("class", name = 'Hardcore{#1}' main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!{#1}"]), sound = s_scream),
                            Quest("class", name = 'Hardcore{#2}' main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = random.choice(["We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!"]), sound = s_scream),                            
                            
                            
                            ]

    return
