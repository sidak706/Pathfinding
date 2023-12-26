package cpen221.mp2.graph;

import java.util.List;
import java.util.Map;
import java.util.Set;

public interface IGraph<V extends Vertex, E extends Edge<V>> {

    /* === TASK 1 === */
    boolean addVertex(V v);
    boolean hasVertex(V v);
    boolean addEdge(E e);
    boolean hasEdge(E e);
    boolean hasEdge(V v1, V v2);
    int edgeLength(V v1, V v2);

    /* === TASK 2 === */
    int edgeLengthSum();
    boolean removeEdge(E e);
    boolean removeEdge(V v1, V v2);
    boolean removeVertex(V v);
    E getEdge(V v1, V v2);
    Set<V> allVertices();
    Set<E> allEdges();
    Set<E> allEdges(V v);
    Map<V, E> getNeighbourhood(V v);

    /* === TASK 3 === */

    int pathCost(List<V> path, PathCostType costType);
    List<V> minimumCostPath(V source, V sink, PathCostType costType);
    Map<V, E> getNeighbourhood(V v, int range);

    /* === TASK 4 === */
    int getDiameter(PathCostType costType);
    V getCenter(PathCostType costType);
}

