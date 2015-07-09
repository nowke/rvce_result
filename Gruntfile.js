module.exports = function(grunt) {

	// require('load-grunt-tasks')(grunt);

	grunt.initConfig({
		sass: {
			options: {
				includePaths: ['rvce_result/static/build/scss']
			},
			dist: {
				options: {
					outputStyle: 'compressed'
				},
				files: {
					'rvce_result/static/dist/css/styles.min.css': 'rvce_result/static/build/scss/styles.scss',
					'rvce_result/static/dist/css/materialize.min.css': 'rvce_result/static/build/scss/materialize.scss',
				}
			}
		},

		copy: {
			main: {
				files: [
					{
						expand: true, 
						cwd: 'rvce_result/static/build/font/', 
						src: ['**'],
						dest: 'rvce_result/static/dist/font',
					},
				],
			},
		},

		watch: {
			grunt: { files: ['Gruntfile.js'] },

			sass: {
				files: 'rvce_result/static/build/scss/**/*.scss',
				tasks: ['sass']
			},
		}
	});

	grunt.loadNpmTasks('grunt-sass');
  	grunt.loadNpmTasks('grunt-contrib-watch');
  	grunt.loadNpmTasks('grunt-contrib-copy');

  	grunt.registerTask('build', ['sass', 'copy']);
	grunt.registerTask('default', ['build', 'watch']);
};