import pygame
import math
import Spot
import algorithms 

def game(win, width):
	ROWS = 100
	grid = Spot.make_grid(ROWS, width)

	start = None
	end = None
  
	run = True
	while run:
		Spot.draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = Spot.get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = Spot.get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1 and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					algorithms.A_star(lambda: Spot.draw(win, grid, ROWS, width), grid, start, end)
				
				if event.key == pygame.K_2 and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					algorithms.Dijkstra(lambda: Spot.draw(win, grid, ROWS, width), grid, start, end)
				
				if event.key == pygame.K_3 and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					algorithms.Best_First(lambda: Spot.draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_4 and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					algorithms.BFS(lambda: Spot.draw(win, grid, ROWS, width), grid, start, end)


				if event.key == pygame.K_q:
					start = None
					end = None
					grid = Spot.make_grid(ROWS, width)

	pygame.quit()


game(Spot.WIN, Spot.WIDTH)