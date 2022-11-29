import { readFileSync } from 'fs'

const data = JSON.parse(readFileSync('./input.json', 'utf8'))
const dataWithIndex = data.map((username, idx) => ({
  username,
  idx,
  isKilled: false
}))

let index = 0
let usersKilled = 0
let hasBeenKilled = false
let hasBeenLooked = false

while (usersKilled < dataWithIndex.length - 1) {
  const indexTo = index % dataWithIndex.length
  const userInfo = dataWithIndex[indexTo]

  if (!userInfo.isKilled && hasBeenLooked && !hasBeenKilled) {
    userInfo.isKilled = true
    usersKilled++
    hasBeenLooked = false
    hasBeenKilled = true
  }
  if (!userInfo.isKilled && !hasBeenLooked) {
    hasBeenLooked = true
    hasBeenKilled = false
  }

  index++
}

const { username, idx } = dataWithIndex.filter(({ isKilled }) => !isKilled)[0]
console.log(`submit ${username}-${idx}`)
