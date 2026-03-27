from queue import PriorityQueue
import pygame

# manhatten distance func
def h(p1, p2):
    x1, y1= p1
    x2, y2= p2
    return abs(x1- x2)+ abs(y1- y2)

def algorithm(draw, grid, start, end):
    count= 0
    open_set= PriorityQueue()
    # (fScore, number of tiles traversed to reach this tile from start tile, tile itself)
    open_set.put((0, count, start))
    came_from= {}
    
    # formula f(T)= h(T)+ g(T)
    
    # gScore is the distance travelled from the start tile
    g_score= {tile: float("inf") for row in grid for tile in row}
    g_score[start]= 0
    
    # fScore is the predicted distance to the end tile
    f_score= {tile: float("inf") for row in grid for tile in row}
    f_score[start]= h(start.get_pos(), end.get_pos())
    
    open_set_hash= {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            # Algorithm Kill Switch
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current= open_set.get()[2]# get current node
        open_set_hash.remove(current)
        
        if current == end:# draw path
            while current in came_from:
                current= came_from[current]
                
                #~ Allways Make Sure That The Data Type Of Current Has An Implementation Of The Bellow Function
                current.make_path()
                
                draw()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score= g_score[current]+ 1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor]= current
                g_score[neighbor]= temp_g_score
                f_score[neighbor]= temp_g_score+ h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count+= 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        
        if current != start:
            current.make_closed()
    return False
    
    
    

def main():
    print("A STAR")
if __name__== "__main__" :
    main()