import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

class Skill2
{
    int id_utente;
    int punteggio;
    String skill;
    public Skill2(int id_utente,int punteggio, String skill)
    {
        this.punteggio = punteggio;
        this.skill = skill;
        this.id_utente = id_utente;
    }
    @Override
    public String toString() {
        return "Skill{id=" + id_utente + ", name='" + skill + "', score=" + punteggio + '}';
    }
}

public class prova2 
{
    public static void main(String[] args) throws IOException 
    {
        int T,M,N,S;
        String[] skillRichieste;
        List<Skill2> skillCandidato;
        
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("4/input/input-1-1.txt")));
        T = Integer.parseInt(br.readLine().trim());

        for(int i=0;i<T;i++)
        {
            String[] secondLine = br.readLine().trim().split(" ");
            N = Integer.parseInt(secondLine[0]);
            M = Integer.parseInt(secondLine[1]);
            S = Integer.parseInt(secondLine[2]);

            skillRichieste = br.readLine().trim().split(" ");

            skillCandidato = new ArrayList<>();
            for (int h = 0; h < N; h++) 
            {
                int id = Integer.parseInt(br.readLine().trim());
                String[] skillData = br.readLine().trim().split(" ");
                String skillName = skillData[0];
                int skillPunteggio = Integer.parseInt(skillData[1]);
                skillCandidato.add(new Skill2(id, skillPunteggio,skillName));
            }

                br.close();

                // Output for verification
                System.out.println("T: " + T);
                System.out.println("N: " + N + ", M: " + M + ", S: " + S);
                System.out.println("Skill Richieste: " + Arrays.toString(skillRichieste));
                for (Skill2 skill : skillCandidato) {
                    System.out.println(skill);
                }

           
            int max = 0;
            int index = 0;
            int punteggioTotale = 0;
            //devo registrare indice utente con relativa skill assegnata e punteggio
            List<Skill2> skillAssegnate = new ArrayList<>();
            //ciclo per ognuna delle skill richieste
            for(int j = 0; j < M; j++)
            {
                max=0;index=0;
                for(int k=0;k<N;k++)
                {
                    //ciclo per tutte le  skill 
                        
                    if(skillCandidato.get(k).skill.equals(skillRichieste[j]))
                    {
                        //devo controllare se nella lista di skill c'è già l'utente
                        //inoltre controllo se il punteggio è maggiore di quello già presente per la skill di quell'utente
                        //se si aggiorno il punteggio e la skill assegnata a quell'utente
                        if(skillCandidato.get(k).punteggio > max && !skillAssegnate.contains(skillCandidato.get(k)))
                        {
                            //ho trovato una skill fra quelle degli utenti che combacia con una di quelle da assegnare e ha un punteggio maggiore del massimo attuala trovato finora
                            max = skillCandidato.get(k).punteggio;
                            index = skillCandidato.get(k).id_utente;
                            skillAssegnate.add(skillCandidato.get(k));
                        }
                    }
                }
                    
                System.out.println("Candidato " + index + " ha la skill " + skillRichieste[j] + " con punteggio " + max);
                punteggioTotale += max;
            }
            System.out.println("Punteggio totale: " + punteggioTotale);
        }
    }  
}