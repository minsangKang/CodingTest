import Foundation

func solution(_ n:Int) -> Int {
    let temp: String = String(String(n, radix: 3).reversed())
    let result: Int = Int(temp, radix: 3)!
    return result
}