public class HashTable <T>{
    private NodoHash[] arreglo;
    private int cont;
    private double factorCarga = 0.8;
    
    public HashTable() {
        cont = 0;
        arreglo = new NodoHash[1];
        arreglo[0] = new NodoHash(null); //centinela
    }
    
    public void insertar(T elem) {
        NodoHash nodo = new NodoHash(elem);
        cont++;
        if((double)cont/arreglo.length > factorCarga)
            expande();
        int pos = elem.hashCode() % arreglo.length;
        NodoHash sig = arreglo[pos].getSig();
        arreglo[pos].setSig(nodo);
        nodo.setSig(sig);
    }

    private void expande() {
        NodoHash[] arregloNuevo = new NodoHash[arreglo.length*2];
        for(int i = 0; i < arregloNuevo.length; i++)
            arregloNuevo[i] = new NodoHash(null);
        for(int i = 0; i < arreglo.length; i++) {
            NodoHash actual = arreglo[i].getSig();
            while(actual != null) {
                int pos = actual.getDato().hashCode() % arregloNuevo.length;
                NodoHash nuevo = new NodoHash(actual.getDato());
                NodoHash sig = arregloNuevo[pos].getSig();
                arregloNuevo[pos].setSig(nuevo);
                nuevo.setSig(sig);
                actual = actual.getSig();
            }
        }
        arreglo = arregloNuevo;
    }
    
    public NodoHash find(T elem) {
        int pos = elem.hashCode() % arreglo.length;
        NodoHash actual = arreglo[pos];
        while(actual.getSig() != null && !actual.getSig().getDato().equals(elem))
            actual = actual.getSig();
        if(actual.getSig() != null && actual.getSig().getDato().equals(elem))
            return actual;
        return null;
    }
    
    public NodoHash<T> eliminar(T elem) {
        NodoHash ant = find(elem);
        if(ant == null)
            return null;
        cont--;
        NodoHash target = ant.getSig();
        NodoHash sig = target.getSig();
        target.setSig(null);
        ant.setSig(sig);
        return target;
    }
    
    public String toString() {
        StringBuilder cad = new StringBuilder();
        for(int i = 0; i < arreglo.length; i++) {
            NodoHash actual = arreglo[i];
            while(actual != null) {
                if(actual.getDato() == null)
                    cad.append("c" + " ");
                else
                    cad.append(actual.getDato() + " ");
                actual = actual.getSig();
            }
            cad.append("\n");
        }
        return cad.toString();
    }    
}