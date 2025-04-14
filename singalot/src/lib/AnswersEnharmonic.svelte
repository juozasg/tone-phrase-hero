<script lang="ts">
	import { germanEnharmonics, germanNames, type Mood, type Semitone } from './names';

	interface Props {
		semitone: Semitone;
		mood: 'happy' | 'sad';
		onAnswered: (correct: boolean) => void;
	}
	const { semitone, mood, onAnswered }: Props = $props();

	const enharmonicNeeded = () => {
		if (mood === 'sad') {
			return semitone === 3 || semitone === 10;
		} else if (mood === 'happy') {
			return semitone === 6;
		}
		return false;
	};
</script>

<div class="answers">
	<!-- C# key -->
	<button class="btn btn-primary" onclick={() => onAnswered(!enharmonicNeeded())}>{germanNames(semitone, mood)}</button>
	<button class="btn btn-primary" onclick={() => onAnswered(enharmonicNeeded())}>{germanNames(semitone, mood)} / {germanEnharmonics(semitone, mood)}</button>
</div>

<style>
	.btn {
		margin: 3px;
	}
	.answers {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}
</style>
