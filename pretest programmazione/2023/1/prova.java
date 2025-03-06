import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class prova 
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br=null;
        try {
            br = new BufferedReader(new InputStreamReader(new FileInputStream("1/input/input-2-0.txt")));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        BufferedReader br2=null;
        try {
            br2 = new BufferedReader(new InputStreamReader(new FileInputStream("1/output/output-2-0.txt")));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        StringTokenizer st=new StringTokenizer(br.readLine());
        int q=Integer.parseInt(st.nextToken());
        int n=Integer.parseInt(st.nextToken());
        String giuste=br.readLine();
        String utente=br.readLine();
        while(utente!=null)
        {
            int punti=0;
            for(int i=0;i<utente.length();i++)
            {
                if(utente.charAt(i)==giuste.charAt(i))
                {
                    punti++;
                }
            }
            int effettivo=Integer.parseInt(br2.readLine());
            if(punti!=effettivo)
            {
                System.out.println("Errore");
            }else {
                System.out.println("Corretto");
            }
            utente=br.readLine();
        }

    }
}
