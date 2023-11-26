from . import models

def starts():
    try:
        message = """                                                                                                                                                                                                                                                                                                                                                                   
        GGGGGGGGGGGGPPPPPPPPPPPPPPPPP  MMMMMMMM               MMMMMMMM     RRRRRRRRRRRRRRRRR                                                     iiii                                     
     GGG::::::::::::P::::::::::::::::P M:::::::M             M:::::::M     R::::::::::::::::R                                                   i::::i                                    
   GG:::::::::::::::P::::::PPPPPP:::::PM::::::::M           M::::::::M     R::::::RRRRRR:::::R                                                   iiii                                     
  G:::::GGGGGGGG::::PP:::::P     P:::::M:::::::::M         M:::::::::M     RR:::::R     R:::::R                                                                                           
 G:::::G       GGGGGG P::::P     P:::::M::::::::::M       M::::::::::M       R::::R     R:::::uuuuuu    uuuuunnnn  nnnnnnnn   nnnn  nnnnnnnn   iiiiiinnnn  nnnnnnnn      ggggggggg   ggggg
G:::::G               P::::P     P:::::M:::::::::::M     M:::::::::::M       R::::R     R:::::u::::u    u::::n:::nn::::::::nn n:::nn::::::::nn i:::::n:::nn::::::::nn   g:::::::::ggg::::g
G:::::G               P::::PPPPPP:::::PM:::::::M::::M   M::::M:::::::M       R::::RRRRRR:::::Ru::::u    u::::n::::::::::::::nnn::::::::::::::nn i::::n::::::::::::::nn g:::::::::::::::::g
G:::::G    GGGGGGGGGG P:::::::::::::PP M::::::M M::::M M::::M M::::::M       R:::::::::::::RR u::::u    u::::nn:::::::::::::::nn:::::::::::::::ni::::nn:::::::::::::::g::::::ggggg::::::gg
G:::::G    G::::::::G P::::PPPPPPPPP   M::::::M  M::::M::::M  M::::::M       R::::RRRRRR:::::Ru::::u    u::::u n:::::nnnn:::::n n:::::nnnn:::::ni::::i n:::::nnnn:::::g:::::g     g:::::g 
G:::::G    GGGGG::::G P::::P           M::::::M   M:::::::M   M::::::M       R::::R     R:::::u::::u    u::::u n::::n    n::::n n::::n    n::::ni::::i n::::n    n::::g:::::g     g:::::g 
G:::::G        G::::G P::::P           M::::::M    M:::::M    M::::::M       R::::R     R:::::u::::u    u::::u n::::n    n::::n n::::n    n::::ni::::i n::::n    n::::g:::::g     g:::::g 
 G:::::G       G::::G P::::P           M::::::M     MMMMM     M::::::M       R::::R     R:::::u:::::uuuu:::::u n::::n    n::::n n::::n    n::::ni::::i n::::n    n::::g::::::g    g:::::g 
  G:::::GGGGGGGG::::PP::::::PP         M::::::M               M::::::M     RR:::::R     R:::::u:::::::::::::::un::::n    n::::n n::::n    n::::i::::::in::::n    n::::g:::::::ggggg:::::g 
   GG:::::::::::::::P::::::::P         M::::::M               M::::::M     R::::::R     R:::::Ru:::::::::::::::n::::n    n::::n n::::n    n::::i::::::in::::n    n::::ng::::::::::::::::g 
     GGG::::::GGG:::P::::::::P         M::::::M               M::::::M     R::::::R     R:::::R uu::::::::uu:::n::::n    n::::n n::::n    n::::i::::::in::::n    n::::n gg::::::::::::::g 
        GGGGGG   GGGPPPPPPPPPP         MMMMMMMM               MMMMMMMM     RRRRRRRR     RRRRRRR   uuuuuuuu  uuunnnnnn    nnnnnn nnnnnn    nnnnniiiiiiiinnnnnn    nnnnnn   gggggggg::::::g 
                                                                                                                                                                                  g:::::g 
                                                                                                                                                                      gggggg      g:::::g 
                                                                                                                                                                      g:::::gg   gg:::::g 
                                                                                                                                                                       g::::::ggg:::::::g                                                                                                                                                               gg:::::::::::::g                                                                                                                                                                         ggg::::::ggg                                                                                                                                                                               gggggg    
"""

        print(message)
        models.create_all()
    except Exception as e:
        print(f"Error starting GPM: {e}")