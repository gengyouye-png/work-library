import pygame, random, math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

particles = []

running = True
while running:
    screen.fill((0, 0, 0))

    if random.random() < 0.05:
        x, y = random.randint(100, 700), random.randint(100, 300)
        color = [random.randint(100,255) for _ in range(3)]
        for _ in range(50):
            angle = random.uniform(0, 2*math.pi)
            speed = random.uniform(2,5)
            particles.append([x, y, angle, speed, 50, color])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_particles = []
    for p in particles:
        x, y, angle, speed, life, color = p
        x += math.cos(angle) * speed
        y += math.sin(angle) * speed
        speed *= 0.98
        life -= 1
        if life > 0:
            pygame.draw.circle(screen, color, (int(x), int(y)), 2)
            new_particles.append([x, y, angle, speed, life, color])

    particles = new_particles

    pygame.display.flip()
    clock.tick(60)

pygame.quit()