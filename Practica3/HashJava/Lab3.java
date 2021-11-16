import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Diego Arellano
 */
public class Lab3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        ArrayList lista = new ArrayList();
        try {
            File file = new File("imdb.csv");
            Scanner scan = new Scanner(file);
            scan.useDelimiter(",");
            scan.nextLine();
            while(scan.hasNext()) {
                lista.add(new Film(scan.next(), scan.next(), scan.next()));
                scan.nextLine();
            }
            scan.close();
        } catch(Exception e) {
            System.out.println("Archivo no encontrado");
        }
        System.out.println(lista.get(1001).toString());
    }
    
}
