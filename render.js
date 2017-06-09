// TODO update path when new version on npm
const MagicEye = require("../MagicEye.js/magiceye.js").MagicEye;
const SAMPLES_PER_DIGIT = 100;
const DIGIT_COUNT = 10;
const WIDTH = 400;
const HEIGHT = 400;

const opts = {
  width: WIDTH,
  height: HEIGHT,
};

for (let i = 0; i < DIGIT_COUNT; i++) {
  opts.text = `${i}`;
  for (let j = 0; j < SAMPLES_PER_DIGIT; j++) {
    opts.output = `../magic-eye-classifier/magic_digits/${i}_${j}`;
    MagicEye.render(opts);
  }
}

