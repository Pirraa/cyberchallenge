import java.util.Arrays;
import java.util.Scanner;

public class prova {
    public static void main(String[] args) {
        int N=6,T=100;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Inserisci secondi massimi");
        T = scanner.nextInt();
        System.out.println("Inserisci numero di servizi");
        N = scanner.nextInt();
        int[] tempi_servizi = new int[N];
        //int[] tempi_servizi={12,49,87,21,11,31};
        /*for(int i=0;i<N;i++)
        {
            System.out.println("Inserisci tempo servizio "+(i+1));
            tempi_servizi[i] = scanner.nextInt();
        }*/
        System.out.println("Inserisci tempi servizi");
        int tempo=scanner.nextInt();
        for(int i=0;i<N;i++)
        {
            tempi_servizi[i]=tempo;
        }

        int somma=Arrays.stream(tempi_servizi).sum();
        boolean bastano;
        int worker=1;
        int maxserviti=0;

        while(true)
        {
            bastano=true;
            int[] tempiWorker=new int[worker];
            for(int i=0;i<worker;i++)
            {
                tempiWorker[i]=0;
            }
            for(int i=0;i<worker && bastano;i++)
            {
                for(int j=maxserviti;j<N;j++)
                {
                    if(tempiWorker[i]+tempi_servizi[j]<=T)
                    {
                        tempiWorker[i]=tempiWorker[i]+tempi_servizi[j];
                        if(j==N-1)
                        {
                            System.out.println("Numero minimo di lavoratori: "+worker);
                            return;
                        }
                    }
                    else
                    {
                        if(i==worker-1)
                        {
                            worker++;
                            bastano=false;
                            maxserviti=0;
                            break;
                        }else{
                            maxserviti=j;
                            if(j==N-1)
                            {
                                System.out.println("Numero minimo di lavoratori: "+worker);
                                return;
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
}
