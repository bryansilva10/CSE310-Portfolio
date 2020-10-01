//set up a proxy to target localhost3000 everytime there is a request (only in dev, not prod)
module.exports = {
	configureWebpack: {
		devServer: {
			proxy: {
				'/api': {
					target: 'http://localhost:3000',
				},
			},
		},
	},
}