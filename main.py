import pygame
from config import settings
from core.state_manager import StateManager
from core.sound_manager import SoundManager

from screens.menu import MenuState

def main():
    pygame.init()
    SoundManager.init()

    SoundManager.play_soundtrack(
        settings.SOUNDTRACK_URL,
        loop= -1,
        volume= settings.MUSIC_VOLUME,
    )
    
    if settings.FULLSCREEN:
        display_info = pygame.display.Info()
        settings.WINDOW_WIDTH = display_info.current_w
        settings.WINDOW_HEIGHT = display_info.current_h
        screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

    pygame.display.set_caption("Jornada Espacial")
    clock = pygame.time.Clock()
    
    # Inicializar o gerenciador de estados
    state_manager = StateManager(MenuState(None))
    state_manager.current_state.manager = state_manager
    
    running = True

    state_manager = StateManager(MenuState(None))
    state_manager.current_state.manager = state_manager
    state_manager.set_state(MenuState(state_manager))

    while running:
        dt = clock.tick(settings.FPS) / 1000 

        # Processar eventos
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)
        state_manager.update(dt)
        state_manager.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
