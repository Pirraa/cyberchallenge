import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class prova2 {
    public static void main(String[] args) throws IOException {
        int N=6,T=100;
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream("3/input/input-2-9.txt")));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        T = Integer.parseInt(tokenizer.nextToken());
        int[] tempi_servizi = new int[N];
        String line=reader.readLine();
        tokenizer = new StringTokenizer(line);
        for(int i=0;i<N;i++)
        {
            tempi_servizi[i] = Integer.parseInt(tokenizer.nextToken());
        }

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
                            reader = new BufferedReader(new InputStreamReader(new FileInputStream("3/output/output-2-9.txt")));
                            int effettivi=Integer.parseInt(reader.readLine());
                            if(effettivi==worker)
                            {
                                System.out.println("Corretto");
                            }else{
                                System.out.println("Sbagliato");
                            }
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
