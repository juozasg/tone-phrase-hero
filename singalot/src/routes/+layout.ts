export const ssr = false;
export const prerender = true;
export const trailingSlash = 'always';

import '$lib/audio.svelte';
import { initAudio } from '$lib/audio.svelte';
// import { SplendidGrandPiano, Reverb } from "smplr";

export async function load() {
	if (typeof AudioContext !== 'undefined') {
		initAudio();

	}
}

