import pygame
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Инициализируем pygame
pygame.init()

# Задаем размер окна в пикселях
size = (640, 480)

# Создаем окно с заданным размером
screen = pygame.display.set_mode(size)

# Устанавливаем заголовок окна
pygame.display.set_caption("Перемещение круга")

# Фоновый цвет
BACKGROUND = (0, 0, 0)

# Цвет круга
CIRCLE_COLOR = (255, 255, 255)

# Радиус круга
CIRCLE_RADIUS = 20

# Загрузка изображения Pacman
pacman = pygame.image.load("pacman.jpg")

# Начальная позиция круга
circle_pos = (320, 240)

# Угол траектории в градусах
angle = 20

# Скорость перемещения за 1 кадр в пикселях
speed = 2

# Расстояние до мыши
dist = 0
max_distance = 500
min_speed = 1
max_speed = 3

# Создание объекта clock для ограничения частоты кадров
clock = pygame.time.Clock()

# Создание цикла для обработки событий и обновления экрана
running = True
while running:
    # Проверка событий клавиатуры и мыши
    for event in pygame.event.get():
        # Выход из цикла при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # Вычисление угла между текущей позицией круга и позицией курсора
    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - circle_pos[0]
    dy = mouse_pos[1] - circle_pos[1]
    angle = math.degrees(math.atan2(dy, dx))

    # Скорость в зависимости от расстояния
    dist = distance(circle_pos, mouse_pos)
    speed = max_speed - (dist / max_distance) * (max_speed - min_speed)
    speed = max(min_speed, min(max_speed, speed))  # Ограничение скорости

    # Вычисление смещения по осям X и Y на основе угла и скорости
    dx = speed * math.cos(math.radians(angle))
    dy = speed * math.sin(math.radians(angle))

    # Обновление позиции круга с учетом смещения по осям X и Y
    circle_pos = (circle_pos[0] + dx, circle_pos[1] + dy)

    # Заполнение фона черным цветом
    screen.fill(BACKGROUND)

    # Рисование повернутого Pacman
    rotated_pacman = pygame.transform.rotate(pacman, -angle)
    rotated_pacman_rect = rotated_pacman.get_rect()
    rotated_pacman_rect.center = circle_pos
    screen.blit(rotated_pacman, rotated_pacman_rect)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров до 60 FPS
    clock.tick(60)

# Завершение работы pygame
pygame.quit()