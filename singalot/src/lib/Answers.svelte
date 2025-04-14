<script lang="ts">
	import type { Semitone } from "./names";

	interface Props {
		answerOnClick: (st: Semitone, mood: 'happy' | 'sad') => void;
	}

	const { answerOnClick }: Props = $props();
</script>

<div class="answers">
	<!-- C# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick(1, 'sad')}>Cis moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick(1, 'happy')}>Des dur</button>

	<!-- D# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick(3, 'sad')}>Dis moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick(3, 'happy')}>Es dur</button>

	<!-- F# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick(6, 'sad')}>Fis moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick(6, 'happy')}>Ges dur</button>

	<!-- G# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick(8, 'sad')}>Gis moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick(8, 'happy')}>As dur</button>

	<!-- A# key -->
	<button class="btn btn-primary" onclick={() => answerOnClick(10, 'sad')}>Ais moll</button>
	<button class="btn btn-primary" onclick={() => answerOnClick(10, 'happy')}>B dur</button>
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
