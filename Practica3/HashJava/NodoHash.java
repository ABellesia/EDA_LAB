public class NodoHash {
    private Film dato;
    private NodoHash sig;
    
    NodoHash(Film dato) {
        this.dato = dato;
    }

    public void setSig(NodoHash sig) {
        this.sig = sig;
    }

    public Film getDato() {
        return dato;
    }

    public NodoHash getSig() {
        return sig;
    }
    
    
}