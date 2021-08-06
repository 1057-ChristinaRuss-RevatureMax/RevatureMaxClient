var bar = new ProgressBar.Circle(loadingcircle, {
  strokeWidth: 6,
  easing: 'easeInOut',
  duration: 10000,  // 10 seconds
  color: '#F26925',
  trailColor: '#B9B9BA',
  trailWidth: 1,
  svgStyle: null
});
bar.animate(1.0);