import java.util.*; 

public class djikstra {
    
    public Stack<Vertex> algorithm(int[][] grid, Vertex source, Vertex target){
        List<Vertex> q = new ArrayList<Vertex>(); 

        getVertices(grid, source, q); // All unvisited nodes

        HashMap<Vertex, Double> vertexToSource = new HashMap<Vertex, Double>(); 

        HashMap<Vertex, Vertex> prevVertex = new HashMap<Vertex, Vertex>(); 

        Stack<Vertex> path = new Stack<Vertex>();

        for (Vertex vertex : q) {
            vertexToSource.put(vertex, Double.POSITIVE_INFINITY); 
            prevVertex.put(vertex, null); 
        }
        vertexToSource.replace(source, 0.0); 

        while (q.size() > 0){

            Vertex u = getMinDistVertex(source, q, vertexToSource); 

            if(u.equals(target)){
                Vertex prev = prevVertex.get(u); 
                System.out.println("(" + prev.getRow() + "," + prev.getCol() + ")");
                getPreviousSet(source, target, u, path, prevVertex);
                break; 
            }

            q.remove(u); 

            List<Vertex> uNeighbours = getNeighboursinQ(u, q); 

            for (Vertex v : uNeighbours) {
                double alt = vertexToSource.get(u) + u.getDistance(v); 
                if(alt < vertexToSource.get(v)){
                    vertexToSource.replace(v, alt); 
                    prevVertex.replace(v, u); 
                }
            }

        }
        // getPreviousSet(source, target, target, path, prevVertex);
        return path; 
    }

    private boolean isCorrect(Vertex source, Stack<Vertex> path){
        for (Vertex vertex : path) {
            if(vertex.equals(source)){
                return true; 
            } 
        }
        return false; 
    }    

    private void getPreviousSet(Vertex source, Vertex target, Vertex vertex, Stack<Vertex> path, Map<Vertex, Vertex> prevSet){
        Vertex previous = prevSet.get(vertex); 
        if(previous == null && (!vertex.equals(source))){
            System.out.println("No path found");
            return ; 
        }
        if(previous.equals(source)){
            path.push(vertex); 
            path.push(previous); 
            return ; 
        }
        path.push(vertex); 
        getPreviousSet(source, target, previous, path, prevSet);
    }

    private Vertex getMinDistVertex(Vertex source, List<Vertex> q, HashMap<Vertex, Double> vTs){

        double minDist = vTs.get(q.get(0));
        Vertex closestVertex = q.get(0); 
        for (Vertex vertex : q) {
            if(vTs.get(vertex) <= minDist){
                minDist = vTs.get(vertex); 
                closestVertex = vertex ;
            }
        }
        return closestVertex; 
    }

    private List<Vertex> getNeighboursinQ(Vertex vertex, List<Vertex> q){
        List<Vertex> neighbours = new ArrayList<Vertex>(); 

        for (Vertex v : q) {
            
            if((vertex.getCol() == v.getCol()) && (Math.abs(vertex.getRow() - v.getRow()) == 1)){
                if(vertex.isVertex()) neighbours.add(v); 
            }

            else if((vertex.getRow() == v.getRow()) && (Math.abs(vertex.getCol() - v.getCol())== 1)){
                if(vertex.isVertex()) neighbours.add(v); 
            }

        }
        return neighbours; 
    }

    private void getVertices(int[][] grid, Vertex source, List<Vertex> q){
        // Getting all vertices in grid (-1 indicates wall)
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if(grid[i][j] != -1){
                    Vertex vertex = new Vertex(i, j, grid[i][j]);
                    q.add(vertex); 
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] arr = {{1,  1, -1, 1, 1},
                       {1,  1, -1, 1, 1},
                       {1,  1, 1, 1, 1},
                       {1,  1, 1, 1, 1},
                       {1,  1, 1, 1, 1},
                      };

        djikstra runner = new djikstra(); 
        Vertex source = new Vertex(0, 0, arr[0][0]); 
        Vertex target = new Vertex(0, 3, arr[0][3]);
        Stack<Vertex> path = runner.algorithm(arr, source, target);

        System.out.println(path.size());
        for (Vertex vertex : path) {
            System.out.print("(" + vertex.getRow() + "," + vertex.getCol() +  ")" + "<--");
        }

    }

}



