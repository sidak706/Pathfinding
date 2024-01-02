public class Vertex {

    private int row, col, value; 

    public Vertex(int row, int col, int value) {
        this.row = row; 
        this.col = col; 
        this.value = value; 
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Vertex) {
            Vertex other = (Vertex) o;
            if (other.getRow() == this.getRow() && other.getCol() == this.getCol()) {
                return true;
            }
        }
        return false;
    }

    @Override
    public int hashCode() {
        return this.row + this.col;
    }

    public int getRow(){
        return this.row; 
    }

    public int getCol(){
        return this.col; 
    }

    public double getDistance(Vertex vertex){
        if(vertex.value == -1){
            return Double.POSITIVE_INFINITY; 
        }
        return (Math.abs(this.row - vertex.row) + Math.abs(this.col - vertex.col)); 
    }

    public boolean isVertex(){
        if(this.value == -1) return false; 
        return true; 
    }

}
