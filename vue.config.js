
//   module.exports = {
//     devServer: {
//       host: '0.0.0.0',
//       port: 443, 
//     },
//   }


//   const fs = require('fs')

// module.exports = {
//     devServer: {
//         open: process.platform === 'darwin',
//         hotOnly: false,
//         host: '0.0.0.0',
//         https:{

//         },
//         port: 80, 
//         }
// }

const fs = require('fs')

module.exports = {
    devServer: {
    port:8080,

    host: '0.0.0.0',
    // key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
    // cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),
    hotOnly: false,
    }
}
// key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
// cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),