import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var count: Int = 0
    var zeroCount: Int = 0
    for lot in lottos {
        if win_nums.contains(lot) {
            count += 1
        }
        else if(lot == 0) {
            zeroCount += 1
        }
    }
    var firstScore: Int = getScore(count+zeroCount)
    var lastScore: Int = getScore(count)
    var result: [Int] = []
    result.append(firstScore)
    result.append(lastScore)
    return result
}

func getScore(_ count: Int) -> Int {
    var score: Int = 0
    switch(count) {
        case 2:
        score = 5
        case 3:
        score = 4
        case 4:
        score = 3
        case 5:
        score = 2
        case 6:
        score = 1
        default:
        score = 6
    }
    return score
}