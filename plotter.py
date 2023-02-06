import pygame, math, random
from point_extractor import randomPoints, extractor



def main():

    pygame.init()

    pygame.display.set_caption("simulation")

    screen = pygame.display.set_mode((888, 888))

    pointsList = []

    cx = 200
    cy = 444

    vals = extractor()
    xvals = vals[0]
    yvals = vals[1]


    tim = 0

    path = []

    def epicycles(cx, cy, vals, phi):

        currx = cx
        curry = cy
        prevx = cx
        prevy = cy

        for ind in range(len(vals['radius'])):

            radius = vals['radius'][ind]
            phase = vals['phase'][ind]
            freq = vals['freq'][ind]

            pygame.draw.arc(screen, (255, 255, 255), (currx - radius, curry - radius, 2*radius, 2*radius), 0, 2*math.pi, 1)

            currx += radius*math.cos(freq*tim + phase + phi)
            curry += radius*math.sin(freq*tim + phase + phi)

            pygame.draw.circle(screen, (255, 255, 255), (currx, curry), 2)
            pygame.draw.line(screen, (255, 255, 255), (prevx, prevy), (currx, curry), 2)

            prevx = currx
            prevy = curry

        return [currx, curry]


    ready = True

    while ready:

        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ready = False

        screen.fill((0,0,0))


        x_epi = epicycles(cx, cy, xvals, math.pi/2)
        y_epi = epicycles(cx + 300, cy - 200, yvals, 0)

        path.insert(0, [y_epi[0], x_epi[1]])

        pygame.draw.line(screen, (255, 255, 255), x_epi, path[0])
        pygame.draw.line(screen, (255, 255, 255), y_epi, path[0])

        if len(pointsList) > 250:
            pointsList.pop()

        for ind in range(len(path)):
            # pygame.draw.circle(screen, (255, 255, 255), (cx + ind + padd, pointsList[ind]), 5)
            if ind != 0:
                pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (path[ind-1]), (path[ind]))

        dt = 2*math.pi/len(xvals['radius'])
        tim += dt

        pygame.display.update()



if __name__ == "__main__":
    main()