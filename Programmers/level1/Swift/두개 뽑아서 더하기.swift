import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    let numbers = numbers.sorted()
    var result: [Int] = []
    
    for i in 0..<numbers.count-1 {
        for j in i+1..<numbers.count {
            let temp = numbers[i]+numbers[j]
            if(!result.contains(temp)) {
                result.append(temp)
            }
        }
    }
    return result.sorted()
}