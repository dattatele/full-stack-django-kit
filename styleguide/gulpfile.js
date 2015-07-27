var gulp = require('gulp');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var less = require('gulp-less');
var minifyCss = require('gulp-minify-css');
var watch = require('gulp-watch');
var nunjucks = require('gulp-nunjucks-html');

var nunjucksOpts = {
    searchPaths: ['src/templates']
};

var BUILD_DEST = 'dist/styleguide';

gulp.task('js', function() {
  return gulp.src('src/**/*.js')
    .pipe(sourcemaps.init())
    .pipe(concat('site.js'))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(BUILD_DEST + '/js'));
});

gulp.task("css", function () {
  return gulp.src(['src/less/main.less'])
    .pipe(sourcemaps.init())
    .pipe(concat('site.css'))
    .pipe(less())
    .pipe(minifyCss())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(BUILD_DEST + '/css'));
});

gulp.task('nunjucks', function() {
    return gulp.src('src/pages/**/*.html')
        .pipe(nunjucks(nunjucksOpts))
        .pipe(gulp.dest(BUILD_DEST));
});

gulp.task('build', ['js', 'css', 'nunjucks']);

gulp.task('watch', function(){
  gulp.watch(['src/js/**/*.js'], ['js']);
    gulp.watch(['src/less/**/*.less'], ['css']);
    gulp.watch(['src/templates/**/*.html', 'src/pages/**/*.html'], ['nunjucks']);
});