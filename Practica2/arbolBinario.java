import java.util.*;

public class LinkedBinaryTree<T> implements BinaryTreeADT<T>{
 NodoBin<T> raiz;
int cont;
  LinkedBinaryTree(){
    raiz=null;
    cont=0;
  }
  LinkedBinaryTree(T elem){
    raiz=new NodoBin<T>(elem);
    cont=1;
  
  public boolean isEmpty(){
    return cont==0;
  }
  public int size(){
    return cont;
  }
  public boolean find(T elem){
      return find(elem, raiz)!=null;
  }
  
  private NodoBin<T> find(T otro, NodoBin<T> hoja){
    if(hoja==null)
      return null;
    
    if(hoja.elem.equals(otro))
      return hoja;  
    
    NodoBin<T> temp=find(otro, hoja.izq);
    if(temp==null)
      temp=find(otro,hoja.der);
    return temp;    
  }



  
  private NodoBin<T> find2(T elem, NodoBin<T> actual){
    if(actual!= null)
      if(actual.getDato().equals(elem))
        return actual;
      NodoBin<T> der = find2(elem, actual.getDer());
      NodoBin<T> izq = find2(elem,actual.getIzq());
      if(der==null)
        return izq;
      return der;
  }

  public Iterator<T> preOrden(){
    ArrayList<T> lista=new ArrayList<T>();


    preOrden(raiz,lista);
    return lista.iterator();

  }
  private void preOrden(NodoBin<T> actual,ArrayList<T> lista){
      if(actual==null)
          return;
      lista.add(actual.getDato());//esto fue visitar
      preOrden(actual.getIzq(),lista);
      preOrden(actual.getDer(),lista);


  }
    public Iterator<T> inOrden(){
    ArrayList<T> lista=new ArrayList<T>();
    inOrden(raiz,lista);
    return lista.iterator();

  }
    private void inOrden(NodoBin<T> actual,ArrayList<T> lista){
      if(actual==null)
          return;
      inOrden(actual.getIzq(),lista);
      lista.add(actual.getDato());//esto fue visitar

      inOrden(actual.getDer(),lista);
  }

public Iterator<T> postOrden(){
    ArrayList<T> lista=new ArrayList<T>();
    postOrden(raiz,lista);
    return lista.iterator();

  }
  private void postOrden(NodoBin<T> actual,ArrayList<T> lista){
      if(actual==null)
          return;
      postOrden(actual.getIzq(),lista);
      postOrden(actual.getDer(),lista);
      lista.add(actual.getDato());//esto fue visitar

      
  }

  public int caminoLargo (){
    return caminoLargo(raiz,0,0);

  }

  private int caminoLargo(NodoBin<T> actual, int cont, int max){

    if(actual.getIzq()!=null){
      cont++;
      if(cont>max)
        caminoLargo(actual.getIzq(), cont, cont);
      else
        caminoLargo(actual.getIzq(), cont, max);
    }
    if(actual.getDer()!=null){
      cont++;
      if(cont>max)
        caminoLargo(actual.getDer(), cont, cont);
      else
        caminoLargo(actual.getDer(), cont, max);
    }
    return cont;


  }


public int altura(){
  if(raiz==null)
    return -1;
  return altura(raiz)-1;
} 
private int altura(NodoBin<T> actual){
  if (actual==null)
    return 0;
  return 1+ Math.max(altura(actual.getIzq()),altura(actual.getDer()));
  

}
private int alturaMasClaro(NodoBin<T> actual){
  if (actual==null)
    return 0;
  int alturaizq=altura(actual.getIzq());
  int alturader=altura(actual.getDer());
  if (alturaizq>alturader)
    return alturaizq+1;
  else
    return alturader+1;

  

}


}