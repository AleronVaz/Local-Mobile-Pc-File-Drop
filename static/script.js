document.addEventListener('DOMContentLoaded', () => {
    // DOM Element Node Declarations
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');
    const infoOpen = document.getElementById('info-open');
    const infoClose = document.getElementById('info-close');
    const infoOverlay = document.getElementById('info-overlay');
    const fileInput = document.getElementById('file-input');
    const dropZone = document.getElementById('drop-zone');
    const uploadForm = document.getElementById('upload-form');
    const statusText = document.getElementById('status-text');
    const fileNameDisplay = document.getElementById('file-name-display');
    const progressContainer = document.getElementById('progress-container');
    const progressBar = document.getElementById('progress-bar');
    const percentDisplay = document.getElementById('percent-display');
    const submitBtn = document.getElementById('submit-btn');

    /* ==========================================================================
       1. CORE THEMING SWITCHENGINE FLOW
       ========================================================================== */
    // Synchronize current local system view parameters
    const savedTheme = localStorage.getItem('localdrop-theme') || 'light';
    body.setAttribute('data-theme', savedTheme);

    themeToggle.addEventListener('click', () => {
        const currentTheme = body.getAttribute('data-theme');
        const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        body.setAttribute('data-theme', nextTheme);
        localStorage.setItem('localdrop-theme', nextTheme);
    });

    /* ==========================================================================
       2. CIRCULAR OVERLAY EXPANSION MANAGEMENT
       ========================================================================== */
    infoOpen.addEventListener('click', () => {
        infoOverlay.classList.add('expanded');
    });

    infoClose.addEventListener('click', () => {
        infoOverlay.classList.remove('expanded');
    });

    /* ==========================================================================
       3. INPUT INTERACTION & VISUAL STATE MANAGEMENT
       ========================================================================== */
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            const file = e.target.files[0];
            
            // Transform drop card visualization to notify presence of selected asset
            dropZone.classList.add('asset-loaded');
            statusText.innerText = "Asset Staged Successfully";
            fileNameDisplay.innerText = `${file.name} (${formatBytes(file.size)})`;
            
            // Enable action controller button execution
            submitBtn.disabled = false;
            submitBtn.innerText = "Initialize Transfer";
            
            // Reset background trackers if a prior upload completed
            progressContainer.classList.add('idles');
            progressBar.style.width = '0%';
            percentDisplay.innerText = '0%';
        }
    });

    // Byte conversion parser helper
    function formatBytes(bytes, decimals = 2) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    /* ==========================================================================
       4. ZERO-REFRESH ASSET STREAMING CORE ENGINE
       ========================================================================== */
    uploadForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Halt standard full page reload hijack 

        const file = fileInput.files[0];
        if (!file) return;

        // Package structural data binary chunk components
        const formData = new FormData();
        formData.append('dropped_file', file);

        // Deploy raw XMLHttpRequest to gain direct hook resolution on network buffers
        const xhr = new XMLHttpRequest();
        
        // Expose visibility track container
        progressContainer.classList.remove('idles');
        submitBtn.disabled = true;
        submitBtn.innerText = "Streaming Data Blocks...";

        // Hook tracking loop mechanisms
        xhr.upload.addEventListener('progress', (event) => {
            if (event.lengthComputable) {
                const percentage = Math.round((event.loaded / event.total) * 100);
                
                // Adjust CSS width layouts
                progressBar.style.width = `${percentage}%`;
                percentDisplay.innerText = `${percentage}%`;
                
                // Shift background gradient position values tracking along the color path
                progressBar.style.backgroundPosition = `${100 - percentage}% 0%`;
            }
        });

        // Capture response resolution hooks
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Success Execution Callback Loop
                    statusText.innerText = "Asset Drop Complete! 🎉";
                    submitBtn.innerText = "Asset Saved To Disk";
                    
                    // Reset inputs safely for subsequent operations
                    fileInput.value = "";
                    dropZone.classList.remove('asset-loaded');
                    
                    setTimeout(() => {
                        submitBtn.innerText = "Staging Awaiting Clear Input";
                    }, 3000);
                } else {
                    // System failure anomaly catch
                    statusText.innerText = "Pipeline Interruption Encountered";
                    submitBtn.innerText = "Retry Interface Transfer";
                    submitBtn.disabled = false;
                    alert(`Network Error Status: ${xhr.status} - Transfer aborted.`);
                }
            }
        };

        // Open structural route network pipes back up to Python
        xhr.open('POST', '/upload', true);
        xhr.send(formData);
    });
});