/* ============================================================================
   PREMIUM HEADER NAVIGATION – INTERACTIONS & SCROLL EFFECTS
   ============================================================================
   
   Sprint D2.1: Premium Header Redesign
   
   Handles:
   - Sticky header behavior (hide top info layer on scroll)
   - Mobile hamburger menu toggle
   - Navigation link active states
   - Scroll shadow effects
   - Keyboard navigation
   - Accessibility (ARIA attributes)
   
   Progressive enhancement - graceful fallback without JavaScript.
   
============================================================================ */

'use strict';

(function() {
    // ========================================================================
    // CONFIGURATION
    // ========================================================================
    
    const SCROLL_THRESHOLD = 50;  // Hide top layer after this many px
    const SCROLL_SHADOW_THRESHOLD = 5;  // Show shadow after this many px
    
    // ========================================================================
    // DOM ELEMENTS
    // ========================================================================
    
    const header = document.querySelector('.header');
    const headerTop = document.getElementById('headerTop');
    const headerNav = document.querySelector('.header-nav');
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    const allNavLinks = document.querySelectorAll('.nav-link');
    
    // Guard: Ensure elements exist
    if (!header || !headerTop || !headerNav || !navToggle || !navLinks) {
        console.warn('Header elements not found');
        return;
    }
    
    // ========================================================================
    // 1. SCROLL HANDLING – Sticky Header Effects
    // ========================================================================
    
    let lastScrollY = 0;
    let ticking = false;
    
    /**
     * Handle scroll events (requestAnimationFrame optimized)
     */
    function handleScroll() {
        const scrollY = window.scrollY;
        
        // Hide header-top after scroll threshold
        if (scrollY > SCROLL_THRESHOLD) {
            headerTop.classList.add('is-hidden');
            header.classList.add('is-sticky');
        } else {
            headerTop.classList.remove('is-hidden');
            header.classList.remove('is-sticky');
        }
        
        // Show shadow on header-nav after scroll
        if (scrollY > SCROLL_SHADOW_THRESHOLD) {
            headerNav.classList.add('is-scrolled');
        } else {
            headerNav.classList.remove('is-scrolled');
        }
        
        lastScrollY = scrollY;
        ticking = false;
    }
    
    /**
     * Optimize scroll event with requestAnimationFrame
     */
    function onScroll() {
        if (!ticking) {
            window.requestAnimationFrame(handleScroll);
            ticking = true;
        }
    }
    
    // Add scroll listener
    window.addEventListener('scroll', onScroll, { passive: true });
    
    // ========================================================================
    // 2. MOBILE HAMBURGER MENU
    // ========================================================================
    
    /**
     * Toggle mobile navigation menu
     */
    function toggleMobileMenu() {
        const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
        
        navToggle.setAttribute('aria-expanded', !isOpen);
        navLinks.setAttribute('aria-expanded', !isOpen);
        navToggle.classList.toggle('is-open');
        navLinks.classList.toggle('is-open');
        
        // Prevent scroll when menu is open
        if (!isOpen) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }
    
    /**
     * Close mobile navigation menu
     */
    function closeMobileMenu() {
        navToggle.setAttribute('aria-expanded', 'false');
        navLinks.setAttribute('aria-expanded', 'false');
        navToggle.classList.remove('is-open');
        navLinks.classList.remove('is-open');
        document.body.style.overflow = '';
    }
    
    /**
     * Toggle menu on button click
     */
    navToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMobileMenu();
    });
    
    /**
     * Close menu when navigation link is clicked
     */
    allNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Close on mobile
            if (window.innerWidth < 768) {
                closeMobileMenu();
            }
        });
    });
    
    /**
     * Close menu on Escape key
     */
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
            if (isOpen) {
                closeMobileMenu();
            }
        }
    });
    
    /**
     * Close menu on outside click
     */
    document.addEventListener('click', (e) => {
        const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
        if (!header.contains(e.target) && isOpen) {
            closeMobileMenu();
        }
    });
    
    /**
     * Close menu on window resize (back to desktop)
     */
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768) {
            closeMobileMenu();
        }
    });
    
    // ========================================================================
    // 3. NAVIGATION ACTIVE STATE
    // ========================================================================
    
    /**
     * Update active navigation link based on current page
     */
    function updateActiveNavLink() {
        const currentPath = window.location.pathname;
        
        allNavLinks.forEach(link => {
            const href = link.getAttribute('href');
            
            // Remove active class from all links
            link.classList.remove('is-active');
            
            // Add active class to current page link
            if (href === currentPath || (href === '/' && currentPath === '/')) {
                link.classList.add('is-active');
            }
        });
    }
    
    // Update active state on page load
    updateActiveNavLink();
    
    // ========================================================================
    // 4. CLOSE MENU ON LINK CLICK FOR INTERNAL NAVIGATION
    // ========================================================================
    
    allNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Small delay to allow navigation before closing
            setTimeout(() => {
                updateActiveNavLink();
            }, 100);
        });
    });
    
    // ========================================================================
    // INITIALIZATION
    // ========================================================================
    
    // Trigger initial scroll check on page load
    handleScroll();
    
    // Expose functions for potential external use
    window.navigationAPI = {
        toggleMenu: toggleMobileMenu,
        closeMenu: closeMobileMenu,
        updateActive: updateActiveNavLink
    };
})();

    
    // ========================================================================
    // 2. STICKY NAVBAR SHADOW ON SCROLL
    // ========================================================================
    
    /**
     * Update navbar appearance on scroll
     */
    function handleScroll() {
        const scrolled = window.scrollY > SCROLL_THRESHOLD;
        
        if (scrolled) {
            navbar.classList.add(SCROLL_CLASS);
        } else {
            navbar.classList.remove(SCROLL_CLASS);
        }
    }
    
    // Add scroll listener with throttling
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
    
    // ========================================================================
    // 3. ACTIVE LINK DETECTION
    // ========================================================================
    
    /**
     * Detect current page and set active link
     */
    function setActiveLink() {
        const currentPath = window.location.pathname;
        
        // Get all nav links
        const allLinks = document.querySelectorAll('[data-active]');
        allLinks.forEach(link => link.removeAttribute('data-active'));
        
        // Set active based on current path
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            
            // Match current page
            if (href === currentPath || (currentPath === '/' && href === '/')) {
                link.setAttribute('data-active', 'true');
            } else if (href !== '/' && currentPath.startsWith(href)) {
                link.setAttribute('data-active', 'true');
            }
        });
    }
    
    // Set active link on page load
    setActiveLink();
    
    // ========================================================================
    // 4. RESIZE HANDLING
    // ========================================================================
    
    /**
     * Handle window resize
     */
    function handleResize() {
        // Close mobile menu if window becomes large enough for desktop
        if (window.innerWidth >= 768) {
            closeMobileMenu();
        }
    }
    
    // Add resize listener with throttling
    let resizeTicking = false;
    window.addEventListener('resize', () => {
        if (!resizeTicking) {
            window.requestAnimationFrame(() => {
                handleResize();
                resizeTicking = false;
            });
            resizeTicking = true;
        }
    }, { passive: true });
    
    // ========================================================================
    // 5. INITIALIZATION
    // ========================================================================
    
    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        setActiveLink();
        handleScroll();
    });
    
    // Expose functions globally for debugging (optional)
    if (window.DEBUG) {
        window.navigation = {
            toggleMenu: toggleMobileMenu,
            closeMenu: closeMobileMenu,
            setActive: setActiveLink,
        };
    }
})();
