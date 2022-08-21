import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.DateFormatSymbols;
import java.util.*;

public class Q6 {
    static final String[] months = DateFormatSymbols.getInstance(Locale.ROOT).getMonths();
    static class Person {
        int YY, MM, DD, PB, sss, G;
        String id;
        int ptr = 0;

        int readInt(int count) {
            return Integer.parseInt(id.substring(ptr, ptr += count));
        }

        Person(String id) {
            this.id = id;
            YY = readInt(2);
            if (YY > 20) YY += 1900;
            else YY += 2000;
            MM = readInt(2);
            DD = readInt(2);
            ptr++;
            PB = readInt(2);
            ptr++;
            sss = readInt(3);
            G = readInt(1);
        }

        @Override
        public String toString() {
            return String.format("%s %s %s %s %s",
                    id,
                    DD,
                    months[MM-1],
                    YY,
                    G % 2 == 0 ? "Female" : "Male"
                    );
        }
    }

    static void Q6(List<String> sb) {
        String[] sarr = String.join("", sb).replaceAll(" ", "").split(";");
        int idLen = "YYMMDD-PB-###G".length();
        String sortByStr = sarr[sarr.length-1].substring(idLen);
        List<Person> personList = new ArrayList<>();
        for (String s : sarr) {
            Person p = new Person(s.substring(0, idLen));
            personList.add(p);
        }
        /*
        Birthdate
        BirthYear
        BirthMonth
        BirthDay
        GenderwithMalefirst
        GenderwithFemalefirst
        */
        HashMap<String, Comparator<Person>> dict = new HashMap<>();
        dict.put("Birthdate", Comparator.comparing(x -> x.YY * 10000 + x.MM * 100 + x.DD));
        dict.put("BirthYear", Comparator.comparing(x -> x.YY));
        dict.put("BirthMonth", Comparator.comparing(x -> x.MM));
        dict.put("BirthDay", Comparator.comparing(x -> x.DD));
        dict.put("GenderwithMalefirst", Comparator.comparing(x -> 1 - x.G % 2));  // odd first
        dict.put("GenderwithFemalefirst", Comparator.comparing(x -> x.G % 2));  // even first
        List<Comparator<Person>> comparators = new ArrayList<>();
        outer:
        for (int i = 0; i < 3; i++) {
            for (String key : dict.keySet()) {
                if (sortByStr.startsWith(key)) {
                    sortByStr = sortByStr.substring(key.length());
                    comparators.add(dict.get(key));
                    continue outer;
                }
            }
            throw new RuntimeException();
        }
        personList.sort((x, y) -> {
            int c = 0;
            for (Comparator<Person> comp : comparators) {
                c = comp.compare(x, y);
                if (c != 0) return c;
            }
            return c;
        });
        for (Person p : personList) {
            System.out.println(p);
        }
    }

    public static void main(String[] args) {
        BufferedReader sr = new BufferedReader(new InputStreamReader(System.in));
        String s = null;
        do {
            try {
                List<String> sb = new ArrayList<>();
                while ((s = sr.readLine()) != null) {
                    if (s.length() != 0) sb.add(s);
                    else if (sb.size() != 0) break;
                }
                Q6(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
