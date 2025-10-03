import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        // 1. Создаем новую хеш-таблицу (HashMap)
        Map<String, Integer> scores = new HashMap<>();

        // 2. Добавляем элементы: put(ключ, значение)
        scores.put("Alice", 95);
        scores.put("Bob", 88);
        scores.put("Charlie", 92);

        // 3. Получаем значение по ключу: get(ключ)
        int aliceScore = scores.get("Alice");
        System.out.println("Оценка Алисы: " + aliceScore); // Вывод: Оценка Алисы: 95

        // 4. Проверяем наличие ключа
        if (scores.containsKey("Bob")) {
            System.out.println("Боб присутствует в таблице."); // Вывод: Боб присутствует в таблице.
        }

        // 5. Удаляем элемент
        scores.remove("Charlie");

        // 6. Итерируем по всем элементам
        System.out.println("Все элементы после удаления:");
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
