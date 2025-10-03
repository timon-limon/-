// Примитивный пример, иллюстрирующий структуру
#include <vector>
#include <list>
#include <string>

// Структура для хранения элемента
template <typename Key, typename Value>
struct HashNode {
    Key key;
    Value value;
};

template <typename Key, typename Value>
class HashTable {
private:
    std::vector<std::list<HashNode<Key, Value>>> table; // Вектор списков для раздельной цепочки
    int tableSize;

    // Пример простой хеш-функции (для целочисленных ключей)
    int hashFunction(Key key) {
        return key % tableSize;
    }

public:
    HashTable(int size) : tableSize(size) {
        table.resize(tableSize);
    }

    // Вставка элемента
    void insert(Key key, Value value) {
        int index = hashFunction(key);
        table[index].push_back({key, value}); // Добавляем в список
    }

    // Поиск элемента
    bool find(Key key, Value& value) {
        int index = hashFunction(key);
        for (const auto& node : table[index]) {
            if (node.key == key) {
                value = node.value;
                return true;
            }
        }
        return false;
    }

    // Удаление элемента (упрощено, нужно реализовать удаление из списка)
    void remove(Key key) {
        int index = hashFunction(key);
        auto& bucket = table[index];
        bucket.remove_if([&](const HashNode<Key, Value>& node){
            return node.key == key;
        });
    }
};
