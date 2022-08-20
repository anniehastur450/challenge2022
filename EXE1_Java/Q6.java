import java.text.DateFormatSymbols;
import java.util.*;
import java.util.function.Function;

public class Q6 {
    static final String[] months = DateFormatSymbols.getInstance().getMonths();
    static class Person {
        int YY;
        int MM;
        int DD;
        int PB;
        int sss;
        int G;
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
    static <T extends Comparable<T>> Comparator<Person> comparatorBy(Function<Person, T> f) {
        return (x, y) -> f.apply(x).compareTo(f.apply(y));
    }

    static void Q6(List<String> sb) {
        String s = String.join("", sb).replaceAll(" ", "").replaceAll(";", "");
        int ptr = 0;
        List<Person> personList = new ArrayList<>();
        while ('0' <= s.charAt(ptr) && s.charAt(ptr) <= '9') {
            Person p = new Person(s.substring(ptr, ptr + 14));
            personList.add(p);
            ptr += 14;
        }
        /*
        Birthdate
        BirthYear
        BirthMonth
        BirthDay
        GenderwithMalefirst
        GenderwithFemalefirst
        */
        HashMap<String, Function<Person, Comparable>> dict = new HashMap<>() {{
            put("Birthdate", (x -> x.YY * 10000 + x.MM * 100 + x.DD));
            put("BirthYear", (x -> x.YY));
            put("BirthMonth", (x -> x.MM));
            put("BirthDay", (x -> x.DD));
            put("GenderwithMalefirst", (x -> 1 - x.G % 2));  // odd first
            put("GenderwithFemalefirst", (x -> x.G % 2));  // even first
        }};
        List<Comparator<Person>> comparators = new ArrayList<>();
        outer:
        for (int i = 0; i < 3; i++) {
            String substr = s.substring(ptr);
            for (String key : dict.keySet()) {
                if (substr.startsWith(key)) {
                    ptr += key.length();
                    Function<Person, Comparable> f = dict.get(key);
                    Comparator<Person> comp = (x, y) -> f.apply(x).compareTo(f.apply(y));
                    comparators.add(comp);
                    continue outer;
                }
            }
            throw new RuntimeException();
        }
        personList.sort((x, y) -> {
            int c = 0;
            for (Comparator<Person> comp : comparators){
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
        Scanner sr = new Scanner(System.in);
        String s = null;
        do {
            try {
                List<String> sb = new ArrayList<>();
                s = null;
                while (sr.hasNextLine()) {
                    s = sr.nextLine();
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
