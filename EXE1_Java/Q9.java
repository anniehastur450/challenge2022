import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class Q9 {
    static class Order {
        String name;
        PriorityQueue<Integer> queue = new PriorityQueue<>(Comparator.reverseOrder());  // this is max heap
        int totalCount = 0;  // waiting for remaining food count
        int waitedMinutes = 0;

        Order(String s) {
            String[] s2 = s.split("#");
            name = s2[0];
            for (String s3 : s2[1].split("%")) {
                int count = Integer.parseInt(s3.split(":")[1]);
                queue.add(count);
                totalCount += count;
            }
        }

        void doWait() {
            if (totalCount == 0) return;
            waitedMinutes += 5;
        }
    }

    static class Cook {
        Order cookingFor;
        int remainingCount = 0;

        void acquireFood(List<Order> orders) {
            if (remainingCount != 0) return;
            for (Order o : orders) {
                if (o.queue.isEmpty()) continue;
                cookingFor = o;
                remainingCount = o.queue.poll();
                return;
            }
        }

        void cook() {
            if (remainingCount == 0) return;
            remainingCount--;
            cookingFor.totalCount--;
        }
    }

    static boolean needWaiting(List<Order> orders) {
        for (Order o : orders) {
            if (o.totalCount > 0) return true;
        }
        return false;
    }

    static void Q9(List<String> sb) {
        String s = String.join("", sb).replaceAll(" ", "");
        List<Order> orders = new ArrayList<>();
        for (String substr : s.split(";")) {
            orders.add(new Order(substr));
        }
        // process order now
        List<Cook> cooks = new ArrayList<>();
        for (int i = 0; i < 3; i++) cooks.add(new Cook());
        while (needWaiting(orders)) {
            for (Cook c : cooks) c.acquireFood(orders);

            for (Order o : orders) o.doWait();
            for (Cook c : cooks) c.cook();
        }
        for (Order o : orders) {
            int hr = 10;
            int min = 0;
            min += o.waitedMinutes;
            hr += min / 60;
            min %= 60;
            System.out.printf("%s can collect food at %02d:%02d\n", o.name, hr, min);
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
                Q9(sb);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (s != null);
    }
}
