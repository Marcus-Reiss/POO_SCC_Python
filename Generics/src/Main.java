import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Dicionario<String, Integer> d = new Dicionario<String, Integer>();

        d.add("calorias", 2900);
        d.add("protein", 183);
        d.add("carbo", 320);
        d.add("gurduris", 176);

        Scanner teclado = new Scanner(System.in);
        String chave = "";

        while (true) {
            System.out.print("Chave (ou s para sair) >> ");
            chave = teclado.next();
            if (chave.equals(""))
                break;
            System.out.printf("Valor: %d", d.get(chave));
        }
    }
}