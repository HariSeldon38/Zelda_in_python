import pygame, sys
from settings import *
from level import Level
from debug import debug

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption("Zelda in Python")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

"""
what to explain in anki card :
different ways we use to get object from file to files
 - creating an instance in init method of a file to access to method of that instance where we create it
 - pass the method as a param without calling it
 Encapsulation OOP principle (def get_cost for example)

inline if statement 
if kiijij : okfrijrf
jnfkjr = k,elfkr if oifoin else kfrio

Idea to implement to improve the game :

Game design ideas : 
            [13:44, 28/07/2025] Au fur et à mesure du jeu on débloque des temples tous éparpillés en bord de map. Chacun de ces temple correspond à une discipline :
            - musique
            - literature
            - skate
            - jeux vidéos
            - programmation
            -
            [13:51, 28/07/2025] Antoine: dans chacune de ces discipline on a un arbre de compétences impossible à maitriser en entier avec plein de chanches dans tout les sens, on est obligé de se spéacialiser.
            Plus on avance et on commence à voir apparaitre un par un des fantôme de notre personnage qui précéde nos pas dans les direction des temples. au début un puis deux etc etc, ces fantome deviennent de plus en plus tangible au ours du jeux (au débbut on ne les remarque même pas, mais leur transparence augmente au cours du temps)
            en non trasnparent ils sont des version plus claire de notre personnage qui lui s'assombrit. (car il ne peut pas les rattraper)
            
            au temp mini jeu à faire pr améliorer compétences; (peut être de juste passer du temps) sauf que cela fait passer le temps plus vite et donc rend les autres fantôme plus tangible
            
            Quand on s'occupe pas de leur compétences, que celle ci n'augmentent pas en XP les fantome deviennent plus tangible et l'XP diminue tout doucment (à peine perceptible mais peuvent passer sous la barre à atteindre de lvl d'avat, dasn ce cas on perds pas le level mais l'xp à gg pr le prochain lvl sera plus grand
            
            quand les fantômes deviennent trop tangible ils se retrounent et se mettent à nous attaquer (comme dans Don't qtarve)
            [13:52, 28/07/2025] Antoine: pour sauvegarder, il faut se coucher dans un lit et atteindre le sommeil : autre map ou il faut atteindre un endroit qui s'appelle le sommeil.
            Au début c'est facile mais les fantôme ici sont plus présent facilement et attaquent vite
            [13:55, 28/07/2025] Antoine: pour la compétence de programmation c'est plu différent: faire comprendre qu'il y a une feature abandonée ou on aurait pu modifier le code du jeu pour le rendre plus simple et résoudre des énigme (faut vrmt qu'on comprennent que ça a été abandonné car on n'arraivait pas à s'approprier le jeux qu'on aurait pas vraiment codé nous même.
            
            à des endoit dans la map on peut décoder le message suivant : "I created this game on my own, I created this game, myself, I am the creator, no one else."
            [13:56, 28/07/2025] Antoine: autre discipline associée à un temple : le dessin, le graphisme, place particulière car impossible (presque) de gg de l'xp dedans et nom des skills dans l'arbre de compétence doivent sembler niais par rapport aux autre, généraux, pour montrer qu'au fond je ne sais pas du tout ce que signifie faire du graphisme.
                        things like :
                            - Put images into canvas
                            - Export drawing to the relevant file format
                            - Move the pencil
                            - create some meaning with colors and shapes

            [21:17, 30/07/2025] Antoine: there is a temple where I need to hurt myself in order to unlock it (or gain xp) there is a riddel :
            
            "The key to this riddle has a "T" shape"
            This temple could represent coc and when entering there is a mini game like coc
            [23:03, 30/07/2025] Antoine: celestial elixir haken en musique de JV

            [00:13, 31/07/2025] Antoine: third thing to implement as weapon  and magic is music, It should not be very difficult to fing music note in px art
            what can it do on the game ? change mood : whith indeed the music playing changed and also maybe a filter on the graphics, 
            sepia for meleancholia music
            dark for eerie and horific music
            bright for cheerfull music
            
            when playing with :
            dark ; enemis stronger but so are you attacks : sort of risk it all to faster combat (add blood particle ?)
            [00:17, 31/07/2025] Antoine: when playing with :
            dark ; enemis stronger but so are you attacks : sort of risk it all to faster combat (add blood particle ?)
            sepia : no enemies no pnj, play in the past but new enemies are coming with the sound of the langoliers
            bright : default version ? 
            tryhard music, red bright colors : enemies faster but so are you and all the cool down, game runs faster (mess with fps ?) (celeste speedrun music ?)
            [18:49, 31/07/2025] Antoine: implementing PNJ
            
            make teir movement random based on slices of my own previous movements
            and every XXX time (random too) they go back to their default place)
            
            def compute path ; method to calc how to get back
            [18:49, 31/07/2025] Antoine: find a way to not make them micmic when I attack


Technical ideas : solve bug, improve quality of life, refactor, game feel etc ect
 - cooldown attack could also be upgraded with speed

"""