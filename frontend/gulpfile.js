'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
//var watch = require('gulp-watch');


const cssDest = 'output';

gulp.task('sass', () => {
    return gulp.src('src/scss/main.scss')
        .pipe(sass())
        .pipe(gulp.dest(cssDest));
});

gulp.task('watch', () => {
    return gulp.watch('src/**/*.scss', gulp.series('sass'));
});
