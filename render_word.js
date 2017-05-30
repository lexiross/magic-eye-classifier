// TODO update path when new version on npm
const MagicEye = require("../MagicEye.js/magiceye.js").MagicEye;
const {Noise} = require("noisejs");
const noise = new Noise(Math.random());

const NUM_COLORS = 15;
const WIDTH = 1280;
const HEIGHT = 960;
const NOISE_SCALE = 4 + randHex(16)

const opts = {
  width: WIDTH,
  height: HEIGHT,
  randomFn: (x, y) => (1 + noise.perlin2(x / NOISE_SCALE, y / NOISE_SCALE)) / 2,
};

opts.colors = generatePalette(NUM_COLORS);
opts.text = process.argv[2].toUpperCase();
opts.output = `../magic-eye-classifier/words/${new Date().toISOString()}`;
MagicEye.render(opts);

function randHex(n=256) {
  return Math.floor(Math.random() * n);
}

function randomRGBa() {
	return [Math.floor(Math.random() * randHex()),
					Math.floor(Math.random() * randHex()),
					Math.floor(Math.random() * randHex()),
					255];
}

function generatePalette(numColors) {
	const palette = [];
	for (let i = 0; i < numColors; i++) {
		palette.push(randomRGBa());
	}
	return palette;
}

