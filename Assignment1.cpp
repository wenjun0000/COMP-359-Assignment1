#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Function to update the order of bed sizes based on their search frequency
void updateOrder(vector<string>& sizes, unordered_map<string, int>& frequencies) {
    sort(sizes.begin(), sizes.end(), [&frequencies](const string& a, const string& b) {
        return frequencies[a] > frequencies[b];  // Sort by search frequency
    });
}

// Function to print the order of bed sizes
void printOrder(const vector<string>& sizes) {
    for (const string& size : sizes) {
        cout << size << ' ';
    }
    cout << endl;
}

int main() {
    // Print welcome message
    cout << "Welcome to UFV SleepCountry!" << endl;
    
    vector<string> sizes = {"Twin", "Full", "Queen", "King", "California King"};
    unordered_map<string, int> frequencies = {{"Twin", 0}, {"Full", 0}, {"Queen", 0}, {"King", 0}, {"California King", 0}};
    
    // Print the initial order of bed sizes
    cout << "Initial bed size order: ";
    printOrder(sizes);
    
    string input;
    cout << "Enter the bed size to search (enter 'q' to quit): ";
    
    while (cin >> input && input != "q") {
        if (frequencies.find(input) != frequencies.end()) {
            frequencies[input]++;
            updateOrder(sizes, frequencies);
            
            cout << "Bed size order after searching " << input << ": ";
            printOrder(sizes);
        } else {
            cout << "Invalid bed size, please try again." << endl;
        }
        
        cout << "Enter the bed size to search (enter 'q' to quit): ";
    }
    
    // Print the final search frequencies
    cout << "Final search frequencies:" << endl;
    for (const auto& pair : frequencies) {
        cout << "Bed size " << pair.first << " searched " << pair.second << " times" << endl;
    }

    return 0;
}

