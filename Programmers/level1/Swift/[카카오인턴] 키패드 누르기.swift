import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var result: String = ""
    var beforeL: (Int, Int) = (4,1)
    var beforeR: (Int, Int) = (4,3)
    let dict: [Int:(Int,Int)] = [1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 7:(3,1), 8:(3,2), 9:(3,3), 0:(4,2)]
    for num in numbers {
        if(num == 1 || num == 4 || num == 7) {
            result.append("L")
            beforeL = dict[num]!
        } else if(num == 3 || num == 6 || num == 9) {
            result.append("R")
            beforeR = dict[num]!
        } else {
            let after = dict[num]!
            
            let left_x = abs(beforeL.0-after.0)
            let left_y = abs(beforeL.1-after.1)
            let termL = left_x+left_y
            
            let right_x = abs(beforeR.0-after.0)
            let right_y = abs(beforeR.1-after.1)
            let termR = right_x+right_y
            
            if(termL < termR) {
                result.append("L")
                beforeL = dict[num]!
            } else if(termL > termR) {
                result.append("R")
                beforeR = dict[num]!
            } else {
                if(hand == "left") {
                    result.append("L")
                    beforeL = dict[num]!
                } else {
                    result.append("R")
                    beforeR = dict[num]!
                }
            }
        }
    }
    return result
}