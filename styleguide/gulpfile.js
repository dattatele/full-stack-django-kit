var gulp = require('gulp');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var less = require('gulp-less');
var minifyCss = require('gulp-minify-css');
var watch = require('gulp-watch');

gulp.task('js', function() {
  return gulp.src('src/**/*.js')
    .pipe(sourcemaps.init())
    .pipe(concat('site.js'))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('dist/js'));
});

gulp.task("css", function () {
  return gulp.src(['src/less/main.less'])
    .pipe(sourcemaps.init())
    .pipe(concat('site.css'))
    .pipe(less())
    .pipe(minifyCss())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('dist/css'));
});

gulp.task('build', ['js', 'css']);

gulp.task('watch', function(){
  gulp.watch(['src/js/**/*.js'], ['js']);
  gulp.watch(['src/less/**/*.less'], ['css']);
});