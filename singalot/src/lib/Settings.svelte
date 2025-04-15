<script lang="ts">
	import { isLoadingAudio } from './audio.svelte';
	import { loadSettingsCookie, saveSettingsCookie, settings } from './settings.svelte';


	loadSettingsCookie();
	$effect(() => {
		saveSettingsCookie(settings);
	});
</script>

{#if isLoadingAudio()}
	<div class="container">Loading audio...</div>
{:else}
	<div class="container">
		<div class="columns">
			<div class="column options-column">OPTIONS</div>
			<div class="column play-chord-column">
				<input id="play-chord" type="checkbox" bind:checked={settings.playChord} />
				<label for="play-chord">Play Chord</label>
			</div>
			<div class="column hide-emoji-column">
				<input id="hide-emoji" type="checkbox" bind:checked={settings.hideEmoji} />
				<label for="hide-emoji">Hide Mood Emoji</label>
			</div>
		</div>
	</div>
{/if}

<style>
	.container {
		position: fixed;
		bottom: 64px;
		left: 0;
		width: 100%;
		color: #777;
	}

	.column {
		display: block;
		justify-content: left;
		text-align: left;
		/* border: 1px solid #ddd; */
		padding: 0;
	}

	.options-column {
		min-width: 90px;
		max-width: 90px;
		font-weight: 500;
		padding-left: 8px;
	}

	.play-chord-column {
		min-width: 106px;
		max-width: 106px;
	}

	.hide-emoji-column {
		min-width: 160px;
		max-width: 160px;
	}

	input[type='checkbox'] {
		position: relative;
		bottom: -1px;
	}

	label {
		cursor: pointer;
	}
</style>
