<script lang="ts">
	import MoodButton from './MoodButton.svelte';
	import PianoOctave from './PianoOctave.svelte';
	import RandomizeDice from './RandomizeDice.svelte';
	import { blackSemitones, getSemitone, type Mood, type Semitone } from './names';

	type Props = {
		onQuestionReset: () => void;
	};
	const { onQuestionReset }: Props = $props();

	let randomizeDice: RandomizeDice;

	// const allChoices = ['C#', 'D#', 'F#', 'G#', 'A#'];
	const allChoices = blackSemitones;
	let unseenChoices = $state<Semitone[]>([...allChoices]);

	let pianoKey = $state<Semitone>();
	let mood: Mood = $state('happy');

	export const getKey = () => {
		return pianoKey;
	};
	export const getMood = () => {
		return mood;
	};

	export function matches(st: Semitone, mood: Mood) {
		return st === pianoKey && mood === mood;
	}

	// export function matchesEnharmonic(st: Semitone, keyEnharmonic: string, mood: Mood) {
	// 	if(mood == 'sad' && st == getSemitone('D#')) {
	// 		return keyEnharmonic === 'Eb'
	// 	}

	// 	if(mood == 'happy' && st == getSemitone('F#')) {
	// 		return keyEnharmonic === 'F#'
	// 	}

	// 	if(mood == 'sad' && st == getSemitone('A#')) {
	// 		return keyEnharmonic === 'B'
	// 	}

	// 	return st === keyEnharmonic;
	// }

	// this will play the dice animation
	export const clickRandomizeDice = () => {
		if (randomizeDice) {
			randomizeDice.handleClick();
		}
	};

	const generateQuestion = () => {
		if (unseenChoices.length === 0) {
			unseenChoices = [...allChoices];
		}
		const randomIndex = Math.floor(Math.random() * unseenChoices.length);
		pianoKey = unseenChoices[randomIndex];
		unseenChoices = unseenChoices.filter((_, index) => index !== randomIndex);

		// favor chaning the mood
		const moodOdds = mood === 'happy' ? 0.3 : 0.7;
		mood = Math.random() < moodOdds ? 'happy' : 'sad';

		onQuestionReset();
	};

	const selectedKeys = $derived.by(() => {
		if (pianoKey) {
			return [pianoKey];
		}
		return [];
	});

</script>




<div class="question">
	<div class="container">
		<div class="columns">
			<div class="column randomize-column col-sm-12 col-4">
				<RandomizeDice bind:this={randomizeDice} size={100} callback={generateQuestion} />
			</div>

			<div class="piano-column column col-sm-12 col-4">
				<PianoOctave selectedSemitones={selectedKeys} width={220} />
			</div>

			<div class="column col-sm-12 col-4">
				<MoodButton mood={mood} hidden={true}/>
			</div>
		</div>
	</div>
</div>

<style>
	.question {
		margin: 20px;
	}

	.column {
		/* border: 1px solid red; */
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 20px;
	}

	.piano-column {
		padding-top: 10px;
	}

	.randomize-column {
		position: relative;
	}
</style>
