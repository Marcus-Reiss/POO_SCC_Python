public class Dicionario<K, V> {

     K[] k;
     V[] v;
     int topo;

    public Dicionario() {
        k = (K[]) new Object[100];
        v = (V[]) new Object[100];
        topo = -1;
    }

    public void add(K chave, V valor) {
        k[topo+1] = chave;
        v[topo+1] = valor;
        topo++;
    }

    public V get (K chave) {
        // contains
        if (!contains(chave)) {
            System.out.println("Chave nao encontrada !");
            return (null);
        }

        for (int j = 0; j < k.length; j++) {
            if (k[j] == chave) {
                return (v[j]);
            }
        }

        System.out.println("Valor nao encontrado !");
        return (null);
    }

    public boolean contains (K chave) {
        for (int j = 0; j < k.length; j++) {
            if (k[j] == chave) {
                return (true);
            }
        }
        return (false);
    }

    public boolean containsValue (V valor) {
        for (int j = 0; j < v.length; j++) {
            if (v[j] == valor) {
                return (true);
            }
        }
        return (false);
    }
}
