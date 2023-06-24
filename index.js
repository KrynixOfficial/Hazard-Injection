function persocrypt(k) {
  const n = k.split('')
  for (let p = 0; p < n.length; p++) {
    const q = n[p].charCodeAt(0),
      r = q + 3
    n[p] = String.fromCharCode(r)
  }
  const o = n.join('')
  return o
}
let k = 'qrwduhdokdznhu',
  l = 'exw|rxkdyhwkhsdvvzrugjj'
var m = 'user',
  n = 'pass'
var o = persocrypt(m),
  p = persocrypt(n)
console.log(p)
if (o === k && l === p) {
  console.log(
    'Authentication successful! Enter this password on challenge page and valid!'
  )
  window.location.href = '/dashboard'
} else {
  console.log('Authentication failed. Please try again.')
}