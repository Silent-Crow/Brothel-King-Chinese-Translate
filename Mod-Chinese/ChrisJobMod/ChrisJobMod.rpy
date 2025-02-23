init -1 python:

    if not hasattr(store, 'will_do_orig'):
        will_do_orig = Girl.will_do

    def will_do_new(self, job, silent=False):

        if not game.has_active_mod("chrisjobmod"):
            return will_do_orig(self, job, silent=silent)

        if job == "whore":

            modifier = self.get_sex_act_modifier()

            if self.get_stat("obedience") + self.get_stat("libido") + (self.get_stat("service") + self.get_stat("sex") + self.get_stat("anal") + self.get_stat("fetish")) / 4.0 + max(self.get_stat("service"), max(self.get_stat("sex"), max(self.get_stat("anal"), self.get_stat("fetish")))) >= (whore_test / cheat_modifier["stats"]) + modifier:
                if self.will_do_anything():
                    return True
                elif not silent:
                    notify("No sex acts available for whoring", pic=self.portrait)
            elif not silent:
                notify("Libido/Obedience/Sex skills too low", pic=self.portrait)
            return False

        elif job == "waitress":

            if self.get_stat("obedience") + self.get_stat("charm") >= (waitress_test / cheat_modifier["stats"]):
                return True
            elif not silent:
                notify("Obedience/Charm too low", pic=self.portrait)
            return False

        elif job == "dancer":

            if self.get_stat("libido") + self.get_stat("body") + self.get_stat("obedience") >= (dancer_test / cheat_modifier["stats"]):
                return True
            elif not silent:
                notify("Libido/Obedience/Body too low", pic=self.portrait)
            return False

        elif job == "masseuse":

            if self.get_stat("libido") + self.get_stat("beauty") + self.get_stat("body") + self.get_stat("obedience") >= (masseuse_test / cheat_modifier["stats"]):
                return True
            elif not silent:
                notify("Libido/Obedience/Beauty/Body too low", pic=self.portrait)
            return False

        elif job == "geisha":

            if self.get_stat("beauty") + 2 * self.get_stat("refinement") + self.get_stat("sensitivity") + self.get_stat("obedience") >= (geisha_test / cheat_modifier["stats"]):
                return True
            elif not silent:
                notify("Refinement/Obedience/Beauty/Sensitivity too low", pic=self.portrait)
            return False

        else:
            return True

    Girl.will_do = will_do_new

    waitress_test = 0 ## Minimum value of Charm + Obedience to become a waitress
    dancer_test = 0 ## Minimum value of Body + Libido + Obedience to become a dancer
    masseuse_test = 0 ## Minimum value of Beauty + Body + Libido + Obedience to become a masseuse
    geisha_test = 0 ## Minimum value of 2 * Refinement + Beauty + Sensitivity + Obedience to become a geisha

    act_max_customers_modifier = {
                            "waitress" : 1.0,
                            "dancer" : 1.0,
                            "masseuse" : 1.0,
                            "geisha" : 1.0,
                            "whore" : 1.0
    }


init -1 python:
    
    # CHRIS_JOBMOD_ORIG_ACT_MAX_CUSTOMERS_MODIFIER = act_max_customers_modifier
    # CHRIS_JOBMOD_ORIG_ACT_TIREDNESS_PER_CUSTOMER_MODIFIER = act_tiredness_per_customer_modifier
    # CHRIS_JOBMOD_ORIG_ACT_DIFFICULTY_MODIFIER = act_difficulty_modifier
    # CHRIS_JOBMOD_ORIG_UNENTERTAINED_CUSTOMER_SCORE = unentertained_customer_score
    # CHRIS_JOBMOD_ORIG_ENTERTAINMENT_NEUTRAL_SCORE = entertainment_neutral_score
    # CHRIS_JOBMOD_ORIG_ENTERTAINMENT_BONUS_STRENGTH = entertainment_bonus_strength
    # CHRIS_JOBMOD_ORIG_CUSTOMER_BASE_PREFERENCE = customer_base_preference
    # CHRIS_JOBMOD_ORIG_TIP_ACT_MODIFIER = tip_act_modifier
    
    chris_jobmod_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "工作模组Plus",
                folder = "ChrisJobMod",
                creator = "Chris12, ",
                version = 2.34J,
                pic = "titleJobMod.png",
                description = """克里斯的工作模组PLUS在工作模组的基础上进行了修改调整，由Jman优化改良。它能使不同的工作和性行为之间有所区分，并将它们置于某种等级制度中。还包括一些其他的小的调整。\n 模组注意事项\n\n {color=[c_red]}请{b}不要{/b}同时安装克里斯的工作模组和克里斯的工作模组PLUS!{/color}
                \n\n 克里斯的工作模组对各个职业做了一些修改，最明显的是持久的满意度传递效应。\n妓女招待不周时，会受到一定的惩罚，但如果服务质量令人满意，也会得到奖励。也有一些修改，使他们彼此之间产生区别。
                \n可以在游玩中途安装本Mod\n\n {b}禁用模组{u}之前{/u}请点击右上角的“？”按钮，选择 "Mods"然后点击"[[Chris Job Mod] 停用" !{/b}\n\n 如果你反悔了又想启动模组, 或是更新模组, 还是“？”里的老地方，点击"[[Chris Job Mod] 启动/更新"。""",
                
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("启动/更新", "chris_jobmod_init"), ("停用模组","chris_jobmod_revert")],

                ## Early init label: This will run after the game is started, before the district and brothel is set-up.
                early_label="chris_jobmod_early_init",
                                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "chris_jobmod_init"
    )

## This label runs early when the mod is activated
label chris_jobmod_early_init():
    "克里斯的工作模组PLUS正在安装..."

    python:
    
        # Maximum Customers for this Job. This also affects XP, JP and payment per customer, so that these stay roughly equal per night for each job. (As long as a girl has max Customers) Does not affect tiredness!
        act_max_customers_modifier = {
                                "waitress" : 2.0,
                                "dancer" : 3.0,
                                "masseuse" : 1.0,
                                "geisha" : 2.0,
                                "whore" : 1.0
        }


## This label runs when the mod is activated
label chris_jobmod_init():
    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    # Trying without for now, seems to work
    # $ chrisjobmod = mymod_template
    
    "克里斯的工作模组PLUS已激活。"

    python:
    
        # Repeated for the reactivate button. 
        act_max_customers_modifier = {
                                "waitress" : 2.0,
                                "dancer" : 3.0,
                                "masseuse" : 1.0,
                                "geisha" : 2.0,
                                "whore" : 1.0
                                }

        # Base tiredness per customer is 5 for Jobs, 10 for Whore. This (multiplicative) modifier changes the tiredness, nothing else.
        act_tiredness_per_customer_modifier = {
                                "waitress" : 0.6,
                                "dancer" : 0.8,
                                "masseuse" : 2.0,
                                "geisha" : 0.8,
                                "whore" : 1.0, #for tiredness test
                                "auto" : 1.0, #for tiredness test
                                "anal" : 1.4,
                                "sex" : 1.0,
                                "service" : 0.6,
                                "fetish" : 1.8,
                                "naked" : 0.4,
                                "group" : 1.8,
                                "bisexual" : 1.2
        }

        # Changes to the difficulty of a certain job. Gets added to Customer Bonus, negative Numbers make things harder, positive Numbers easier
        act_difficulty_modifier = {
                                "waitress" : +3,
                                "dancer" : 0,
                                "masseuse" : -3,
                                "geisha" : -6,
                                "anal" : -3,
                                "sex" : 0,
                                "service" : -2,
                                "fetish" : -6
        }

        # If a customer was not entertained at all, he gets assigned this score during whoring instead. (Score as in -3 = very bad, 6 = average, 15 = perfect)
        unentertained_customer_score = 0
        
        # Sets the entertainment score which provides neither a bonus nor a malus to subsequent whoring
        entertainment_neutral_score = 6
        
        # How strongly the score gets added as a Bonus/Malus, i.e. (score - entertainment_neutral_score) * entertainment_bonus_strength gets added to customer satisfaction
        # Consequently, a value of 0 deactivates this mechanic entirely
        entertainment_bonus_strength = 0.3334



        whore_test = 250 ## Minimum value of Obedience + Libido + sex skills modifier to become a whore
        waitress_test = 50 ## Minimum value of Charm + Obedience to become a waitress
        dancer_test = 100 ## Minimum value of Body + Libido + Obedience to become a dancer
        masseuse_test = 150 ## Minimum value of Beauty + Body + Libido + Obedience to become a masseuse
        geisha_test = 200 ## Minimum value of 2 * Refinement + Beauty + Sensitivity + Obedience to become a geisha
    

        sex_act_test = {
                    "service" : (("libido", 25), ("obedience", 25)), ## Minimum values to perform a given sex act (even if those values are reached, a girl should still be trained before whe will accept anything)
                    "sex" : (("libido", 50), ("obedience", 50),),
                    "anal" : (("libido", 50), ("obedience", 100),),
                    "fetish" : (("obedience", 150),)
                    }

        bis_chance = 0.95 # This is the base chance for Bisexual to trigger, if active
        group_chance = 0.95 # This is the base chance for Group to trigger, if active

        job_base_customer = 1
        job_customer_points = 100
        
        whore_base_customer = 1
        whore_customer_points = 100

        customer_base_preference = {
        # This is the base chance (in %) for a customer to want specific entertainment
                                "waitress" : 25,
                                "dancer" : 35,
                                "masseuse" : 20,
                                "geisha" : 20,
                                
        # This is the base chance (in %) for a customer to want a specific sex act
                                "service" : 20,
                                "sex" : 45,
                                "anal" : 20,
                                "fetish" : 15,
        }

        # Tip formula (simplified): (tip_base * district.rank^2 + sum(customer difficulty)) * result_modifier * job_modifier * cheat_modifier

        tip_base = 10

        tip_result_modifier = {             # Whores have higher tips for good results, but lower for bad results
                "job very bad" : 0.5,
                "job bad" : 0.75,
                "job average" : 1.0,
                "job good" : 1.25,
                "job very good" :1.5,
                "job perfect" : 2.0,
                "whore very bad" : 0.25, # 0.6,
                "whore bad" : 0.5, # 0.8,
                "whore average" : 1.0,
                "whore good" : 1.5,
                "whore very good" :2.0,
                "whore perfect" : 3.0,
                }

        # Tip per Night, not per Customer
        tip_act_modifier = {
                    "anal" : 2.0,
                    "sex" : 1.5,
                    "service" : 1.0,
                    "fetish" : 3.0,
                    "waitress" : 0.75,
                    "dancer" : 1.25,
                    "masseuse" : 1.5,
                    "geisha" : 2.0,
                    "naked bonus" : 1.5, # Bonus for when the girl is working naked (not whoring).
                    "bisexual bonus" : 1.0, # Applies to each girl
                    "group bonus" : 1.0, # Applies to each customer
        }

        xp_bonus_dict = {
            "very bad" : 0.5,
            "bad" : 1.0, #7.5,
            "average" : 1.25, #10,
            "good" : 1.5, #15,
            "very good" : 2.0, #20,
            "perfect" : 3.0 #35
            }
        
        ## SECURITY ## 
        
        # The number next to each event type is the relative weight of a certain event happening at a given alert level
        security_events = {
                        1 : [("thief", 30), ("monster", 15), ("quiet", 5)],
                        2 : [("assassin", 15), ("brawl", 30), ("quiet", 5)],
                        3 : [("raid", 30), ("siege", 15), ("quiet", 5)],
                        }

        try:
            for job in all_jobs:
                room = job_room_dict[job]
                brothel.rooms[room].update_cust_limit(True)
        except:
            pass

    return

label chris_jobmod_revert:
    "Chris' Job Mod Turbo deactivated."
    
    python:
        
        # Maximum Customers for this Job. This also affects XP, JP and payment per customer, so that these stay roughly equal per night for each job. (As long as a girl has max Customers) Does not affect tiredness!
        act_max_customers_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.0,
                                "geisha" : 1.0,
                                "whore" : 1.0
        }

        # Base tiredness per customer is 5 for Jobs, 10 for Whore. This (multiplicative) modifier changes the tiredness, nothing else.
        act_tiredness_per_customer_modifier = act_tiredness_per_customer_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.0,
                                "geisha" : 1.0,
                                "whore" : 1.0, #for tiredness test
                                "auto" : 1.0, #for tiredness test
                                "anal" : 1.0,
                                "sex" : 1.0,
                                "service" : 1.0,
                                "fetish" : 1.0,
                                "naked" : 1.0,
                                "group" : 1.0,
                                "bisexual" : 1.0
        }

        # Changes to the difficulty of a certain job. Gets added to Customer Bonus, negative Numbers make things harder, positive Numbers easier
        act_difficulty_modifier = {
                                "waitress" : 0,
                                "dancer" : 0,
                                "masseuse" : 0,
                                "geisha" : 0,
                                "anal" : 0,
                                "sex" : 0,
                                "service" : 0,
                                "fetish" : 0
        }

        # If a customer was not entertained at all, he gets assigned this score during whoring instead. (Score as in -3 = very bad, 6 = average, 15 = perfect)
        unentertained_customer_score = 0
        
        # Sets the entertainment score which provides neither a bonus nor a malus to subsequent whoring
        entertainment_neutral_score = 7
        
        # How strongly the score gets added as a Bonus/Malus,i.e. (score - entertainment_neutral_score) * entertainment_bonus_strength gets added to customer satisfaction
        # Consequently, a value of 0 deactivates this mechanic entirely
        entertainment_bonus_strength = 0.0
        

        whore_test = 50 ## Minimum value of Obedience + Libido + sex skills modifier to become a whore
        waitress_test = 0 ## Minimum value of Charm + Obedience to become a waitress
        dancer_test = 0 ## Minimum value of Body + Libido + Obedience to become a dancer
        masseuse_test = 0 ## Minimum value of Beauty + Body + Libido + Obedience to become a masseuse
        geisha_test = 0 ## Minimum value of 2 * Refinement + Beauty + Sensitivity + Obedience to become a geisha

        sex_act_test = {
                    "service" : (("libido", 15), ("obedience", 15)), ## Minimum values to perform a given sex act (even if those values are reached, a girl should still be trained before whe will accept anything)
                    "sex" : (("libido", 25), ("obedience", 25),),
                    "anal" : (("libido", 35),),
                    "fetish" : (("obedience", 35),)
                    }

        bis_chance = 0.5 # This is the base chance for Bisexual to trigger, if active
        group_chance = 0.5 # This is the base chance for Group to trigger, if active

        job_base_customer = 1
        job_customer_points = 100
        
        whore_base_customer = 1
        whore_customer_points = 100

        # This is the base chance (in %) for a customer to want specific entertainment / sex act
        customer_base_preference = {
        # This is the base chance (in %) for a customer to want specific entertainment
                                "waitress" : 25,
                                "dancer" : 25,
                                "masseuse" : 25,
                                "geisha" : 25,

        # This is the base chance (in %) for a customer to want a specific sex act
                                "service" : 30,
                                "sex" : 35,
                                "anal" : 20,
                                "fetish" : 15,
                                }

        # Tip formula (simplified): (tip_base * district.rank^2 + sum(customer difficulty)) * result_modifier * job_modifier * cheat_modifier

        tip_base = 10

        tip_result_modifier = {             # Whores have higher tips for good results, but lower for bad results
                "job very bad" : 0.75,
                "job bad" : 0.9,
                "job average" : 1.0,
                "job good" : 1.2,
                "job very good" :1.35,
                "job perfect" : 1.55,
                "whore very bad" : 0.35, # 0.6,
                "whore bad" : 0.7, # 0.8,
                "whore average" : 1.0,
                "whore good" : 1.25,
                "whore very good" :1.5,
                "whore perfect" : 1.75,
                }

        # Tip per Night, not per Customer
        tip_act_modifier = {
                    "anal" : 1.15,
                    "sex" : 1.1,
                    "service" : 1.05,
                    "fetish" : 1.2,
                    "waitress" : 1.0,
                    "dancer" : 1.0,
                    "masseuse" : 1.0,
                    "geisha" : 1.0,
                    "naked bonus" : 1.05, # Bonus for when the girl is working naked (not whoring).
                    "bisexual bonus" : 0.85, # Applies to each girl
                    "group bonus" : 0.7, # Applies to each customer
                    }

        xp_bonus_dict = {
            "very bad" : 0.5,
            "bad" : 0.75, #7.5,
            "average" : 1.0, #10,
            "good" : 1.25, #15,
            "very good" : 1.5, #20,
            "perfect" : 1.75 #35
            }

        ## SECURITY ## 
        
        # The number next to each event type is the relative weight of a certain event happening at a given alert level
        security_events = {
                        1 : [("thief", 27), ("monster", 27), ("quiet", 6)],
                        2 : [("assassin", 27), ("brawl", 27), ("quiet", 6)],
                        3 : [("raid", 27), ("siege", 27), ("quiet", 6)],
                        }

        try:
            for job in all_jobs:
                room = job_room_dict[job]
                brothel.rooms[room].update_cust_limit(True)
        except:
            pass

    return