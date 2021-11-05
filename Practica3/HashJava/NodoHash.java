public class NodoHash<T> {
    private T dato;
    private NodoHash<T> sig;
    
    NodoHash(T dato) {
        this.dato = dato;
    }

    public void setSig(NodoHash<T> sig) {
        this.sig = sig;
    }

    public T getDato() {
        return dato;
    }

    public NodoHash<T> getSig() {
        return sig;
    }
    
    
}
