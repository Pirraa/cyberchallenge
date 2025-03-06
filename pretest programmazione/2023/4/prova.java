import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

class Skill
{
    int id_utente;
    int punteggio;
    String skill;
    public Skill(int id_utente,int punteggio, String skill)
    {
        this.punteggio = punteggio;
        this.skill = skill;
        this.id_utente = id_utente;
        }
}

public class prova 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        //Map <Integer,Skill[]> idCandidatoSkill = new HashMap<>();
        int N=14,M=10,S=1,T=1;
        /*System.out.println("Inserisci numero di testcases:");
        T = sc.nextInt();*/
        for(int i=0;i<T;i++)
        {
            /*System.out.println("Inserisci numero candidati:");
            N = sc.nextInt();
            System.out.println("Inserisci numero di scelti:");
            M = sc.nextInt();
            System.out.println("Inserisci numero di skill per candidati:");
            S = sc.nextInt();*/

            /*String skillRichieste[] = new String[M];
            Skill [] skillCandidato = new Skill[S];
            for(int j = 0; j < M; j++)
            {
                System.out.println("Inserisci skill richiesta" + (i+1) + ":");
                skillRichieste[j] = sc.next();
            }*/
            String[] skillRichieste = {"CRY", "MOB", "FOR", "MOB", "MOB", "WEB", "MSC", "WEB", "CRY", "WEB", "NET", "REV", "PWN", "OSI"};

            /*for(int k=0;k<N;k++)
            {
                System.out.println("Inserisci id user " + (k+1) + ":");
                int id=sc.nextInt();
                for(int j = 0; j < S; j++)
                {
                    System.out.println("Inserisci skill user " + (k+1) + ":");
                    String skillName = sc.next();
                    int skillPunteggio = sc.nextInt();
                    skillCandidato[j] = new Skill(id,skillPunteggio, skillName);
                }
                //idCandidatoSkill.put(id, skillCandidato);
            }*/
            Skill[] skillCandidato = {
                new Skill(1, 98, "WEB"),
                new Skill(2, 14, "FOR"),
                new Skill(3, 82, "MSC"),
                new Skill(4, 9, "MSC"),
                new Skill(5, 90, "OSI"),
                new Skill(6, 52, "FOR"),
                new Skill(7, 95, "MSC"),
                new Skill(8, 85, "NET"),
                new Skill(9, 46, "REV"),
                new Skill(10, 16, "CRY"),
                new Skill(11, 32, "MOB"),
                new Skill(12, 41, "PWN"),
                new Skill(13, 59, "CRY"),
                new Skill(14, 34, "CRY")
            };
           
            //sorto le skill in ordine decrescente
            /*Arrays.sort(skillRichieste);
            //sorto le skill dei candidati prima per skill e poi per punteggio
            Arrays.sort(skillCandidato, (a, b) -> {
                int skillComparison = a.skill.compareTo(b.skill);
                if (skillComparison == 0) {
                    return b.punteggio - a.punteggio;
                }
                return skillComparison;
            });
           
            //prendo da lista skillcandidato la prima skill per punteggio di ognuna delle skill
            Map<String, Skill> bestSkills = new HashMap<>();
            for (Skill skill : skillCandidato) {
                if (!bestSkills.containsKey(skill.skill) || bestSkills.get(skill.skill).punteggio < skill.punteggio) {
                    bestSkills.put(skill.skill, skill);
                }
            }*/

            //cerco le skill presenti in skillrichieste ma non in bestskills e le aggiungo con punteggio 0


            /*
             * ad ogni candidato devo assegnare una delle skill richieste 
             * scelgo il candidato con il punteggio più alto per ogni skill e glela assegno
             * sommo i punti totali 
             */

             /*
              * per ogni skill richiesta cerco nell'array di skillcandidato l'id del candidato e il relativo punteggio
              massimo per quella skill, poi controllo se nella lista di skill assegnate c'è già l'utente e se il punteggio
              massimo appena trovato è maggiore di quello già presente, se si aggiorno il punteggio e la skill assegnata a
              inserisco questa skill in una lista di skill assegnate e sommo il punteggio
              *
              */
            int max = 0;
            int index = 0;
            int punteggioTotale = 0;
            //devo registrare indice utente con relativa skill assegnata e punteggio
            List<Skill> skillAssegnate = new ArrayList<>();
            //ciclo per ognuna delle skill richieste
            for(int j = 0; j < M; j++)
            {
                max=0;index=0;
                for(int k=0;k<N;k++)
                {
                    //ciclo per tutte le  skill 
                    
                        if(skillCandidato[k].skill.equals(skillRichieste[j]))
                        {
                            //devo controllare se nella lista di skill c'è già l'utente
                            //inoltre controllo se il punteggio è maggiore di quello già presente per la skill di quell'utente
                            //se si aggiorno il punteggio e la skill assegnata a quell'utente
                            if(skillCandidato[k].punteggio > max && !skillAssegnate.contains(skillCandidato[k]))
                            {
                                max = skillCandidato[k].punteggio;
                                index = skillCandidato[k].id_utente;
                                skillAssegnate.add(skillCandidato[k]);
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